import csv
from operator import itemgetter

import matplotlib.pyplot as plt
import array
import statistics
import numpy as np
from sklearn.linear_model import LinearRegression

timestamps = array.array('d')
distances = array.array('i')
strengths = array.array('i')
eventBoundaries = array.array('d')
eventBoundariesDiscarded = array.array('d')
firstTimestamp = 0


def readData():
    global timestamps, distances, strengths, firstTimestamp
    with open('data/front_70cm_largerangle.csv') as f:
        reader = csv.reader(f, delimiter=';')
        for line in reader:
            if firstTimestamp == 0:
                firstTimestamp = float(line[0])
            timestamps.append(float(line[0]))
            distances.append(int(line[1]))
            strengths.append(int(line[2]))


def plotData():
    adjustedTimestamps = array.array('d')
    for ts in timestamps:
        adjustedTimestamps.append(ts - firstTimestamp)
    plt.scatter(adjustedTimestamps, distances, c=strengths)
    plt.xlabel('wallclock since start [seconds]')
    plt.ylabel('distance [cm]')
    clb = plt.colorbar()
    clb.ax.set_title('strength')
    for t in eventBoundaries:
        plt.axvline(x=t - firstTimestamp, color='b')
    for t in eventBoundariesDiscarded:
        plt.axvline(x=t - firstTimestamp, color='y')
    plt.show()


def analyzeData():
    deltatimes = array.array('d')
    lagging = 0
    event = list()
    for (ts, dist, stren) in zip(timestamps, distances, strengths):
        if lagging == 0:
            lagging = ts
            continue
        deltatime = ts - lagging
        if deltatime > 0.1:
            if eventHandler(event) != 0:
                eventBoundariesDiscarded.append(ts)
            else:
                eventBoundaries.append(ts)

            event = list()
        if 0.0001 < deltatime < 0.1:
            deltatimes.append(deltatime)
        lagging = ts
        event.append((ts, dist, stren))
    print('guessed framerate = %f' % (1 / statistics.median(deltatimes)))
    print('guessed street middle = %d' % (statistics.median(distances)))


def maxStrengthSpeed(event):
    event.sort(key=itemgetter(2), reverse=True)
    xx = array.array('d')
    yy = array.array('d')
    topPoints = round(len(event) * 0.2)
    for i in range(topPoints):
        xx.append(event[i][0])
        yy.append(event[i][1])
    x = np.array(xx)
    y = np.array(yy)
    x = x.reshape(-1, 1)
    model = LinearRegression()
    model.fit(x, y)
    print('R^2: %f points included: %d' % (model.score(x, y), topPoints))
    return model.coef_ / 100 * 3.6

def fromMiddleDistanceSpeed(event):
    startmeasure = event[0]
    endmeasure = event[len(event) - 1]
    mindist = 50000
    maxdist = 0
    for m in event:
        if m[1] < mindist:
            mindist = m[1]
        if m[1] > maxdist:
            maxdist = m[1]
    middledistance = (maxdist + mindist) / 2
    i = 0
    if startmeasure[1] < endmeasure[1]:
        for m in event:
            if m[1] >= middledistance:
                break
            i += 1
    else:
        for m in event:
            if m[1] <= middledistance:
                break
            i += 1
    xx = array.array('d')
    yy = array.array('d')
    for j in range(i-5, i+5):
        xx.append(event[j][0])
        yy.append(event[j][1])
    x = np.array(xx)
    y = np.array(yy)
    x = x.reshape(-1, 1)
    model = LinearRegression()
    model.fit(x, y)
    print('R^2: %f middle point: %d' % (model.score(x, y), i))
    return model.coef_ / 100 * 3.6

discardedEvents = 0
totalEvents = 0


def eventHandler(event):
    global discardedEvents, totalEvents
    totalEvents += 1
    startmeasure = event[0]
    endmeasure = event[len(event) - 1]
    if startmeasure[1] > endmeasure[1]:
        guessedDirection = 'TOWARDS'
    else:
        guessedDirection = 'AWAY'
    mindist = 50000
    maxdist = 0
    minstren = 70000
    maxstren = 0
    for m in event:
        if m[1] < mindist:
            mindist = m[1]
        if m[1] > maxdist:
            maxdist = m[1]
        if m[2] < minstren:
            minstren = m[2]
        if m[2] > maxstren:
            maxstren = m[2]
    measuredDistance = maxdist - mindist
    duration = endmeasure[0] - startmeasure[0]
    print('duration %f' % (duration))
    print('start distance: %5d end distance: %5d points: %4d' % (startmeasure[1], endmeasure[1], len(event)))
    print('minimum distan: %5d maximum dist: %5d measure dist: %5d' % (mindist, maxdist, measuredDistance))
    print('minimum streng: %5d maximum stre: %5d' % (minstren, maxstren))
    if len(event) < 10 or measuredDistance < 150 or duration > 10.0:
        print('discarded.')
        discardedEvents += 1
        return 1
    print('accepted.')
    speed = maxStrengthSpeed(event)
    speed2 = fromMiddleDistanceSpeed(event)
    print('speed: %f or %f direction %s' % (speed, speed2, guessedDirection))
    return 0


if __name__ == '__main__':
    readData()
    analyzeData()
    print("total events: %d discarded events: %d" % (totalEvents, discardedEvents))
    plotData()
