import serial
import serial.tools.list_ports
from time import sleep


def openLidar():
    comports = serial.tools.list_ports.comports();
    for i in comports:
        print(i)

    comports = serial.tools.list_ports.grep('CH340');
    comportList = list(comports)
    portname = comportList[0].device

    ser = serial.Serial(portname, 115200,
                        bytesize=serial.EIGHTBITS,
                        parity=serial.PARITY_NONE,
                        stopbits=serial.STOPBITS_ONE,
                        timeout=None)
    return ser


def initLidar(ser):
    ser.write(b'\xAA\x55\xF0\x00\xFF\xFF\xFF\xFF')  # reset
    sleep(1)
    ser.write(b'\xAA\x55\xF0\x00\x01\x00\x00\x02')  # start config
    sleep(0.5)
    # ser.write(b'\x5A\x05\x05\x02\x66') #text output
    ser.write(b'\x5A\x05\x05\x01\x65')  # standard output
    sleep(0.5)
    ser.write(b'\x5A\x06\x03\x28\x00\x00')  # set frame rate to 40 per second 5A 06 03 LL HH 00
    sleep(0.5)
    ser.write(b'\xAA\x55\xF0\x00\x00\x00\x00\x02')  # end config
    sleep(0.5)


def findStart(ser):
    while True:
        b = b'\x00'
        while b != b'\x59':
            b = ser.read()
        b = ser.read()
        if b == b'\x59':
            break
    ser.read(7)


def getDatagram(ser, datafunc, eventfunc):
    datagram = ser.read(9)
    #print(datagram.hex(':'))
    distL = datagram[2]
    distH = datagram[3]
    strengthL = datagram[4]
    strengthH = datagram[5]
    tempL = datagram[6]
    tempH = datagram[7]
    checksum = datagram[8]
    sum = 0
    for i in range(8):
        sum += datagram[i]
    sum = sum & 0xFF
    if checksum == sum:
        datafunc(distH * 256 + distL, strengthH * 256 + strengthL, tempH * 256 + tempL)
    else:
        eventfunc('checksum failure. reset.')
        findStart(ser)


def processData(distance, strength, temperature):
    print('distance: %d strength: %d temperature: %d' % (distance, strength, temperature))


def processEvent(event):
    print('something happened: %s' % event)


if __name__ == '__main__':
    serial = openLidar()
    initLidar(serial)
    findStart(serial)
    while True:
        getDatagram(serial, processData, processEvent)


