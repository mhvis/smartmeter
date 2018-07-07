import serial
import re

# Possible smart meter configurations
DSMR22 = {"baudrate": 9600,
        "bytesize": serial.SEVENBITS,
        "parity": serial.PARITY_EVEN,
        "stopbits": serial.STOPBITS_ONE}
DSMR40 = {"baudrate": 115200,
        "bytesize": serial.EIGHTBITS,
        "parity": serial.PARITY_NONE,
        "stopbits": serial.STOPBITS_ONE}
DSMR42 = DSMR40
ESMR50 = DSMR40

class SmartMeter(serial.Serial):
    """Extension of the Serial class that adds a readmeter method."""

    def readmeter(self):
        """Reads the next data message on the serial connection. Returns a
        tuple with (header, data). Header is the header string and data is a
        dictionary with OBIS => list of arguments. Arguments of type float*unit
        (e.g. 123*kW) are converted to a tuple of the form (float, string)."""
        # Read until /
        line = ""
        while not line.startswith("/"):
            line = self.readline().decode()

        # Populate header
        header = line[1:].strip()

        # Skip empty line after header
        self.readline()

        # Read lines and populate dictionary until !
        data = {}
        line = self.readline().decode()
        while not line.startswith("!"):
            # Get OBIS
            next_obis = line[:line.index("(")]
            if next_obis:
                obis = next_obis
                data[obis] = []
            # Get and loop over the arguments
            args = re.findall("\(([^()]*)\)", line)
            for arg in args:
                # Do some basic conversions
                valwithunit = re.match("^([0-9.]+)\*([a-zA-Z]+)$", arg)
                if valwithunit:
                    arg = float(valwithunit[1]), valwithunit[2]
                # Save argument with corresponding OBIS
                data[obis].append(arg)
            line = self.readline().decode()
        return header, data
