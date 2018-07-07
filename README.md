# smartmeter

Library for reading smart readers that follow Dutch Smart Meter Requirements
using a P1 port.

## As command-line application

When invoked on the command-line, the application prints the next data message
from the smart meter and exits. The command-line arguments are for specifying
the required settings for the serial connection.

    $ python3 smartmeter.py -h

    usage: smartmeter.py [-h] [-p PORT] [-c {dsmr20,dsmr42,esmr50}]
                         [--baudrate BAUDRATE]
                         [--bytesize {fivebits,sixbits,sevenbits,eightbits}]
                         [--parity {none,even,odd,mark,space}]
                         [--stopbits {one,one_point_five,two}]

    optional arguments:
      -h, --help            show this help message and exit
      -p PORT, --port PORT  serial device name, e.g. /dev/ttyUSB0 or COM3
                            (default: /dev/ttyUSB0)
      -c {dsmr20,dsmr42,esmr50}, --configuration {dsmr20,dsmr42,esmr50}
                            choose a preset configuration for baudrate, bytesize,
                            parity and stopbits (default: esmr50)
      --baudrate BAUDRATE
      --bytesize {fivebits,sixbits,sevenbits,eightbits}
      --parity {none,even,odd,mark,space}
      --stopbits {one,one_point_five,two}

## Library

The library exports a SmartMeter class which is an extension of the Serial
class. It adds a readmeter() method.

