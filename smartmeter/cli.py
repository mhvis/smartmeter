import smartmeter
import serial
import argparse
import pprint
import json # todo make use of this

def cli():
    """CLI application that simply prints a data message."""
    parser = argparse.ArgumentParser(
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-p", "--port", default="/dev/ttyUSB0",
            help="serial device name, e.g. /dev/ttyUSB0 or COM3")
    parser.add_argument("-c", "--configuration", default="esmr50",
            choices=["dsmr22", "dsmr40", "dsmr42", "esmr50"],
            help="choose a preset configuration for baudrate, bytesize, parity and stopbits")
    parser.add_argument("--baudrate", type=int)
    parser.add_argument("--bytesize",
            choices=["fivebits", "sixbits", "sevenbits", "eightbits"])
    parser.add_argument("--parity",
            choices=["none", "even", "odd", "mark", "space"])
    parser.add_argument("--stopbits",
            choices=["one", "one_point_five", "two"])
    args = parser.parse_args()

    # Convert CLI flags to configuration
    presets = {"dsmr22": smartmeter.DSMR22,
            "dsmr40": smartmeter.DSMR40,
            "dsmr42": smartmeter.DSMR42,
            "esmr50": smartmeter.ESMR50}
    configuration = presets[args.configuration]
    if args.baudrate:
        configuration["baudrate"] = args.baudrate
    if args.bytesize:
        bytesizes = {"fivebits": serial.FIVEBITS,
                "sixbits": serial.SIXBITS,
                "sevenbits": serial.SEVENBITS,
                "eightbits": serial.EIGHTBITS}
        configuration["bytesize"] = bytesizes[args.bytesize]
    if args.parity:
        parities = {"none": serial.PARITY_NONE,
                "even": serial.PARITY_EVEN,
                "odd": serial.PARITY_ODD,
                "mark": serial.PARITY_MARK,
                "space": serial.PARITY_SPACE}
        configuration["parity"] = parities[args.parity]
    if args.stopbits:
        stopbits = {"one": serial.STOPBITS_ONE,
                "one_point_five": serial.STOPBITS_ONE_POINT_FIVE,
                "two": serial.STOPBITS_TWO}
        configuration["stopbits"] = stopbits[args.stopbits]

    # Run
    sm = smartmeter.SmartMeter(args.port, timeout= 60, **configuration)
    result = sm.readmeter()
    pprint.pprint(result)
