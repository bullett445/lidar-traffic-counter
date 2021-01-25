import array
from operator import itemgetter
import numpy as np

from sklearn.linear_model import LinearRegression


class Event:
    def __init__(self, e):
        self.event = e.copy()
        self.startmeasurement = self.event[0]
        self.endmeasurement = self.event[len(self.event) - 1]
        self.startTs = self.startmeasurement[0]
        self.endTs = self.endmeasurement[0]
        self.duration = self.endTs - self.startTs
        if self.startmeasurement[1] > self.endmeasurement[1]:
            self.guessedDirection = 'TOWARDS'
        else:
            self.guessedDirection = 'AWAY'
        self.mindistance = 50000
        self.maxdistance = 0
        self.minstrength = 70000
        self.maxstrength = 0
        for m in self.event:
            if m[1] < self.mindistance:
                self.mindistance = m[1]
            if m[1] > self.maxdistance:
                self.maxdistance = m[1]
            if m[2] < self.minstrength:
                self.minstrength = m[2]
            if m[2] > self.maxstrength:
                self.maxstrength = m[2]
        self.measuredDistance = self.maxdistance - self.mindistance

    def getSpeedFromMaxStrength(self):
        sortedEvent = self.event.copy()
        sortedEvent.sort(key=itemgetter(2), reverse=True)
        xx = array.array('d')
        yy = array.array('d')
        topPoints = round(len(sortedEvent) * 0.2)
        for i in range(topPoints):
            xx.append(sortedEvent[i][0])
            yy.append(sortedEvent[i][1])
        x = np.array(xx)
        y = np.array(yy)
        x = x.reshape(-1, 1)
        model = LinearRegression()
        model.fit(x, y)
        r2 = model.score(x, y)
        speed = model.coef_[0] / 100 * 3.6
        return speed, r2, topPoints

    def __str__(self):
        return 'duration %f\nstart distance: %5d end distance: %5d points: %4d\n'\
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


