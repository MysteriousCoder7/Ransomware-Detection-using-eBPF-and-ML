from bcc import BPF
import os
import subprocess
import time

# Start the simulator.py process using subprocess
simulator_process = subprocess.Popen(["python3", "simulator.py"])

# Wait a little for the process to start and get its PID
simulator_pid = simulator_process.pid

# eBPF program
program = r"""
#include <linux/ptrace.h>
#include <linux/sched.h>
#include <linux/utsname.h>
#include <linux/unistd.h>
#include <linux/uaccess.h>

BPF_HASH(syscall_count, u64, u64);
BPF_PROG_ARRAY(syscall_tailcalls, 256);

// General syscall handler
int trace_syscalls(struct bpf_raw_tracepoint_args *ctx) {
    u64 pid_tgid = bpf_get_current_pid_tgid();
    u64 pid = pid_tgid >> 32;

    // Filter for the specific PID (simulator.py)
    if (pid != TARGET_PID) {
        return 0;
    }

    int syscall_nr = ctx->args[1];
    u64 count = 0;
    u64 *current_count = syscall_count.lookup_or_try_init(&syscall_nr, &count);

    if (current_count) {
        (*current_count)++;
    }

    // Log the syscall count for debugging
    bpf_trace_printk("Syscall %d executed by PID: %llu\n", syscall_nr, pid);

    // If this is an execve syscall, redirect to the tailcall handler
    if (syscall_nr == __NR_execve) {
        syscall_tailcalls.call(ctx, 0);
        return 0;
    }

    return 0;
}

// Execve-specific handler
int handle_execve(struct bpf_raw_tracepoint_args *ctx) {
    u64 pid_tgid = bpf_get_current_pid_tgid();
    u64 pid = pid_tgid >> 32;

    char filename[256];
    bpf_probe_read_user(&filename, sizeof(filename), (void *)ctx->args[0]);

    bpf_trace_printk("Execve: PID: %llu, Filename: %s\n", pid, filename);
    return 0;
}
"""

# Replace TARGET_PID in the eBPF code with the simulator.py PID
program = program.replace("TARGET_PID", str(simulator_pid))

# Load the eBPF program
b = BPF(text=program)

# Attach the main syscall handler
b.attach_raw_tracepoint(tp="sys_enter", fn_name="trace_syscalls")

# Load the execve-specific handler and set it as a tailcall target
execve_fn = b.load_func("handle_execve", BPF.RAW_TRACEPOINT)
tailcall_table = b.get_table("syscall_tailcalls")
tailcall_table[0] = execve_fn

# Display logs
print(f"Monitoring system calls for PID {simulator_pid}. Press Ctrl+C to stop.")
b.trace_print()

# Wait for the simulator process to finish (optional)
simulator_process.wait()
