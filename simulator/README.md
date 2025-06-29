# Simulator

## Installation

```shell
python3 -m pip install -r requirements.txt
```

## Encrypt files

```shell
# encrypt temporary files in /tmp/tmpxxx
./simulator.py --password xu18d7wfe2edt

# encrypt files in given directory
./simulator --dir /path/to/dir --password xu18d7wfe2edt
```

## Decrypt files

```shell
# decrypt temporary files in /tmp/tmpxxx
./simulator.py --mode decrypt --password xu18d7wfe2edt

# decrypt files in given directory
./simulator.py --mode decrypt --dir /path/to/dir --password xu18d7wfe2edt
```

## Tracing python execution flow

```shell
./simulator.py --password b12hn736bxe & sudo uflow -l python $!
```
