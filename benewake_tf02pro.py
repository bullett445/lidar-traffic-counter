#
# module reading a Benewake TF 02 pro
#
import serial
import serial.tools.list_ports
from time import sleep
from serial.tools.list_ports_common import ListPortInfo

DISTANCE = 0
STRENGTH = 1
TEMPERATURE = 2

port: serial.Serial = None
inSync = False


class LidarNotFoundException(Exception):
    pass


class LidarReadException(Exception):
    pass


def openLidar():
    global port
    #comports = serial.tools.list_ports.comports()
    #for i in comports:
    #    print(i)

    comports = serial.tools.list_ports.grep('CH340|ttyAMA0')
    comportList: list[ListPortInfo] = list(comports)
    if len(comportList) < 1:
        raise LidarNotFoundException("No CH340 or ttyAMA0 in comport list.")

    portName = comportList[0].device

    port = serial.Serial(portName, 115200,
                         bytesize=serial.EIGHTBITS,
                         parity=serial.PARITY_NONE,
                         stopbits=serial.STOPBITS_ONE,
                         timeout=None)

    port.write(b'\xAA\x55\xF0\x00\xFF\xFF\xFF\xFF')  # reset
    sleep(1)
    port.write(b'\xAA\x55\xF0\x00\x01\x00\x00\x02')  # start config
    sleep(0.5)
    # ser.write(b'\x5A\x05\x05\x02\x66') #text output
    port.write(b'\x5A\x05\x05\x01\x65')  # standard output
    sleep(0.5)
    port.write(b'\x5A\x06\x03\x64\x00\x00')  # set frame rate to 100 per second 5A 06 03 LL HH 00
    sleep(0.5)
    port.write(b'\xAA\x55\xF0\x00\x00\x00\x00\x02')  # end config
    sleep(0.1)


def findStart():
    global port
    port.reset_input_buffer()
    while True:
        b = b'\x00'
        while b != b'\x59':
            b = port.read()
        b = port.read()
        if b == b'\x59':
            break
    port.read(7)


def readDatagram():
    global port, inSync
    if not inSync:
        findStart()
        inSync = True
    datagram = port.read(9)
    # print(datagram.hex(':'))
    distL = datagram[2]
    distH = datagram[3]
    strengthL = datagram[4]
    strengthH = datagram[5]
    tempL = datagram[6]
    tempH = datagram[7]
    checksum = datagram[8]
    checksumCalculated = 0
    for i in range(8):
        checksumCalculated += datagram[i]
    checksumCalculated = checksumCalculated & 0xFF
    if checksum == checksumCalculated:
        return distH * 256 + distL, strengthH * 256 + strengthL, tempH * 256 + tempL
    else:
        inSync = False
        raise LidarReadException("checksum error.")


if __name__ == '__main__':
    openLidar()
    while True:
        try:
            print(readDatagram())
        except:
            print('Exception.')
