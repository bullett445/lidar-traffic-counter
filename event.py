import array
from operator import itemgetter

import matplotlib.colors
import numpy as np
import matplotlib.pyplot as plt


class EventTooSmallException(Exception):
    pass


TIMESTAMP = 0
DISTANCE = 1
STRENGTH = 2
INDEX = 3
VALIDITY = 4


class Event:
    def __init__(self, e):
        self.numberOfPoints = len(e)
        self.event = list()
        for (elem, i) in zip(e, range(len(e))):
            self.event.append([elem[TIMESTAMP], elem[DISTANCE], elem[STRENGTH], i, True])
        self.startmeasurement = self.event[TIMESTAMP]
        self.endmeasurement = self.event[len(self.event) - 1]
        self.startTs = self.startmeasurement[TIMESTAMP]
        self.endTs = self.endmeasurement[TIMESTAMP]
        self.duration = self.endTs - self.startTs
        if self.startmeasurement[DISTANCE] > self.endmeasurement[DISTANCE]:
            self.guessedDirection = 'TOWARDS'
        else:
            self.guessedDirection = 'AWAY'
        self.mindistance = 50000
        self.maxdistance = 0
        self.minstrength = 70000
        self.maxstrength = 0
        for m in self.event:
            if m[DISTANCE] < self.mindistance:
                self.mindistance = m[DISTANCE]
            if m[DISTANCE] > self.maxdistance:
                self.maxdistance = m[DISTANCE]
            if m[STRENGTH] < self.minstrength:
                self.minstrength = m[STRENGTH]
            if m[STRENGTH] > self.maxstrength:
                self.maxstrength = m[STRENGTH]
        self.measuredDistance = self.maxdistance - self.mindistance
        self.limitDistance = 0.1 * self.measuredDistance + self.mindistance
        if self.guessedDirection == 'TOWARDS':
            refStart = self.seekSideReflectionStart(self.event)
            for i in range(refStart, len(self.event)):
                self.event[i][VALIDITY] = False
            self.validPointsCount = refStart
        else:
            refStart = len(self.event) - self.seekSideReflectionStart(reversed(self.event))
            for i in range(0, refStart):
                self.event[i][VALIDITY] = False
            self.validPointsCount = len(self.event) - refStart
        print(self.event)

    def getSpeedFromMaxStrength(self, plot=False):
        def sortKey(e):
            if e[VALIDITY]:
                return e[STRENGTH] + 100000
            else:
                return e[STRENGTH]

        sortedEvent = self.event.copy()
        sortedEvent.sort(key=sortKey, reverse=True)
        xx = array.array('d')
        yy = array.array('d')
        topPoints = round(self.validPointsCount * 0.4)
        for i in range(topPoints):
            xx.append(sortedEvent[i][INDEX])
            yy.append(sortedEvent[i][DISTANCE])
        x = np.array(xx)
        y = np.array(yy)
        model = np.polyfit(x, y, 1)
        r = np.corrcoef(x, y)[0, 1]
        r2 = r ** 2
        speed = model[0] * 3.6
        if plot:
            matrix = np.array(sortedEvent)
            colorNormalizer = matplotlib.colors.Normalize(self.minstrength, self.maxstrength)
            plt.scatter(matrix[:topPoints, INDEX], matrix[:topPoints, DISTANCE],
                        c=matrix[:topPoints, STRENGTH], norm=colorNormalizer, marker='^')
            plt.scatter(matrix[topPoints:self.validPointsCount, INDEX], matrix[topPoints:self.validPointsCount, DISTANCE],
                        c=matrix[topPoints:self.validPointsCount, STRENGTH], norm=colorNormalizer, marker='o')
            plt.scatter(matrix[self.validPointsCount:, INDEX],
                        matrix[self.validPointsCount:, DISTANCE],
                        c=matrix[self.validPointsCount:, STRENGTH], norm=colorNormalizer, marker='+')
            plt.plot(matrix[:, 3], model[0] * matrix[:, INDEX] + model[1], linewidth=0.5)
            plt.axhline(self.limitDistance)
            plt.xlabel('frame id in event')
            plt.ylabel('distance [cm]')
            plt.ylim([self.mindistance - 10, self.maxdistance + 10])
            clb = plt.colorbar()
            clb.ax.set_title('strength')

            plt.show()

        return {"speed": speed, "r2": r2, "numberOfPoints": topPoints}

    def seekSideReflectionStart(self, event):
        i = 0
        for e in event:
            if e[1] < self.limitDistance:
                return i
            i += 1

    def __str__(self):
        return 'duration %f\nstart distance: %5d end distance: %5d points: %4d\n' \
               'minimum distan: %5d maximum dist: %5d measure dist: %5d\nminimum streng: %5d maximum stre: %5d\n' % \
               (self.duration, self.startmeasurement[1], self.endmeasurement[1], len(self.event), self.mindistance,
                self.maxdistance, self.measuredDistance, self.minstrength, self.maxstrength) + \
               str(self.event)

    def getStartDistance(self):
        return self.startmeasurement[1]

    def getEndDistance(self):
        return self.endmeasurement[1]

    def getDuration(self):
        return self.duration

    def getMinDistance(self):
        return self.mindistance

    def getMaxDistance(self):
        return self.maxdistance

    def getMeasuredDistance(self):
        return self.measuredDistance

    def getMinStrength(self):
        return self.minstrength

    def getMaxStrength(self):
        return self.maxstrength

    def getDirection(self):
        return self.guessedDirection

    def getStartTimestamp(self):
        return self.startTs

    def getEndTimestamp(self):
        return self.endTs

    def getNumberOfPoints(self):
        return self.numberOfPoints
