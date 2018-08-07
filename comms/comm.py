import serial
import time


class Lidar(object):
    prefix = b'0xA5'
    commands = {
        "start": b'0x60',
        "stop": b'0x65',
        "device_info": b'0x90',
        "health": b'0x91',
        "reboot": b'0x40'
    }

    def __init__(self, port, baudrate=9600, timeout=None, write_timeout=None):
        self.serial = serial.Serial(port)

    def write(self, payload):
        print("payload: {}".format(payload))
        num_bytes_written =  self.serial.write(payload)
        print("Number of bytes written: {}".format(num_bytes_written))

    def read(self, size):
        self.serial.read(size)

    def shutdown(self):
        self.serial.close()

    def scan(self):
        """
        Send a message to scan and then do something.
        """
        print("starting scan")
        self.write(self.prefix + self.commands["start"])
        print("scan started")

    def stop_scan(self):
        """
        Stop lidar scanning.
        """
        print("stopping scan")
        self.write(self.prefix + self.commands["stop"])
        print("scan stopped")


if __name__ == "__main__":
    lidar = Lidar(port="/dev/ttyACM0")

    lidar.scan()
    time.sleep(5)
    lidar.stop_scan()
