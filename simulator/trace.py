import time
import subprocess
from bcc import BPF

program = """
int trace(struct bpf_raw_tracepoint_args *ctx) {
    u32 pid = bpf_get_current_pid_tgid() >> 32;
    int opcode = ctx->args[1];
    bpf_trace_printk("%d", opcode);
    return 0;
}
"""

b = BPF(text=program)
b.attach_raw_tracepoint(tp="sys_enter", fn_name="trace")

proc = subprocess.Popen("python3 simulator.py --password 1234 --dir TestFolder", shell=True)

logs = []
start = time.time()
while time.time() - start < 2:
    (task, pid, cpu, flags, ts, msg) = b.trace_fields()
    if pid == proc.pid:
        logs.append(str(msg))

syscalls_map = {}

with open("syscallsagni.txt") as f:
    for line in f:
        syscall, number = line.split()
        syscalls_map[number] = syscall

for log in logs:
    number = log[2:-2]
    if number in syscalls_map:
        print(f"{syscalls_map.get(number)}")
    else:
        print(f"{number}")

