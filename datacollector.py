from time import time
import benewake_tf02pro as lidar


def logTimestamp(f, data):
    f.write('t;%f;%d\n' % (time(), data[2]))


def logError(f):
    f.write('f;checksum;%f\n' % (time()))


def logData(f, data):
    f.write('d;%d;%d\n' % (data[0], data[1]))


activeEvent = False
voidDistance = 600  # default 4500 = 45m

if __name__ == '__main__':
    lidar.openLidar()

    with open('c:/lidar/lidar.csv', 'a') as file:
        while True:
            try:
                datapoint = lidar.readDatagram()
                if datapoint[0] < voidDistance:
                    if not activeEvent:
                        activeEvent = True
                        logTimestamp(file, datapoint)
                    logData(file, datapoint)
                else:
                    if activeEvent:
                        activeEvent = False
                        logTimestamp(file, datapoint)
                        file.flush()
                print(datapoint)
            except lidar.LidarReadException:
                logError(file)
                activeEvent = False
                print('read error.')
