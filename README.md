# send-rcon
This program sends commands using the [Source RCON Protocol](https://developer.valvesoftware.com/wiki/Source_RCON_Protocol).

An example of a supported game is minecraft.

## Usage
Command line help is shown below.
```
$ ./send_rcon.py --help
usage: send_rcon.py [-h] [--tls] [--skip-tls-verify]
                    (--file FILE | --command COMMAND)
                    address port

send command using rcon protocol

positional arguments:
  address            target host address
  port               target host port

optional arguments:
  -h, --help         show this help message and exit
  --tls              enable tls
  --skip-tls-verify  skip tls verify
  --file FILE        use command file
  --command COMMAND  command to execute
```

You can create programs using functions as well as commands. For example like this `wakitsubushi.py`.

This script can prevent monsters from being generated.

