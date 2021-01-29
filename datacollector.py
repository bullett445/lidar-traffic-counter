from time import time
import benewake_tf02pro as lidar


def logTimestamp(f, data):
    f.write('t;%f;%d\n' % (time(), data[lidar.TEMPERATURE]))


def logError(f):
    f.write('f;checksum;%f\n' % (time()))


def logData(f, data):
    f.write('d;%d;%d\n' % (data[lidar.DISTANCE], data[lidar.STRENGTH]))


activeEvent = False
voidDistance = 600  # default 4500 = 45m

if __name__ == '__main__':
    print('Initializing...')
    lidar.openLidar()
    print('Fetching Data...')
    with open('c:/lidar/lidar.csv', 'a') as file:
        while True:
            try:
                datapoint = lidar.readDatagram()
                if datapoint[lidar.DISTANCE] < voidDistance:
                    if not activeEvent:
                        activeEvent = True
                        logTimestamp(file, datapoint)
                    logData(file, datapoint)
                else:
                    if activeEvent:
                        activeEvent = False
                        logTimestamp(file, datapoint)
                        file.flush()
                if activeEvent:
                    print('%4.2fm %5d %s' % (datapoint[lidar.DISTANCE] / 100,
                                             datapoint[lidar.STRENGTH], "=" * round(datapoint[lidar.STRENGTH] / 170)))
            except lidar.LidarReadException:
                logError(file)
                activeEvent = False
                print('read error.')
