import csv

import matplotlib.pyplot as plt
import array
import statistics

from event import Event, EventTooSmallException

timestamps = array.array('d')
distances = array.array('i')
strengths = array.array('i')
eventBoundaries = array.array('d')
eventBoundariesDiscarded = array.array('b')
firstTimestamp = 0


def readDataOldFormat():
    global timestamps, distances, strengths, firstTimestamp
    with open('data/old format/front_70cm_largerangle.csv') as f:
        reader = csv.reader(f, delimiter=';')
        for line in reader:
            if firstTimestamp == 0:
                firstTimestamp = float(line[0])
            timestamps.append(float(line[0]))
            distances.append(int(line[1]))
            strengths.append(int(line[2]))


def readData():
    global timestamps, distances, strengths, firstTimestamp
    with open('data/2lane_front.csv') as f:
        reader = csv.reader(f, delimiter=';')
        for line in reader:
            entryType = line[0]
            if entryType == 's':
                eventTimestamp = float(line[1])
                if firstTimestamp == 0:
                    firstTimestamp = eventTimestamp
            elif entryType == 'e':
                pass
            elif entryType == 'd':
                timestamps.append(eventTimestamp)
                distances.append(int(line[1]))
                strengths.append(int(line[2]))
                eventTimestamp += 0.01
            elif entryType == 'f':
                pass
            else:
                print('unknown entry.')
                exit(1)


def plotData():
    adjustedTimestamps = array.array('d')
    for ts in timestamps:
        adjustedTimestamps.append(ts - firstTimestamp)
    plt.scatter(adjustedTimestamps, distances, c=strengths)
    plt.xlabel('wallclock since start [seconds]')
    plt.ylabel('distance [cm]')
    clb = plt.colorbar()
    clb.ax.set_title('strength')
    for i in range(len(eventBoundaries)):
        plt.text(eventBoundaries[i] - firstTimestamp, 100, str(i))
        if eventBoundariesDiscarded[i]:
            plt.axvline(x=eventBoundaries[i] - firstTimestamp, color='y')
        else:
            plt.axvline(x=eventBoundaries[i] - firstTimestamp, color='b')
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
            eventBoundaries.append(ts)
            if eventHandler(event) != 0:
                eventBoundariesDiscarded.append(True)
            else:
                eventBoundariesDiscarded.append(False)

            event = list()
        if 0.0001 < deltatime < 0.1:
            deltatimes.append(deltatime)
        lagging = ts
        event.append((ts, dist, stren))
    print('guessed framerate = %f' % (1 / statistics.median(deltatimes)))
    print('guessed street middle = %d' % (statistics.median(distances)))


discardedEvents = 0
totalEvents = 0
trimOffFirst = 5
trimOffLast = 2

def eventHandler(eventData):
    global discardedEvents, totalEvents
    totalEvents += 1
    print("-- %d ---------------------------------" % totalEvents)

    if len(eventData) < trimOffLast + trimOffFirst + 10:
        print('too short.')
        discardedEvents += 1
        return 1

    event = Event(eventData[trimOffFirst:len(eventData)-trimOffLast])
    print(event)

    if event.getNumberOfPoints() < 10 \
            or event.getMeasuredDistance() < 150 \
            or event.getDuration() > 10.0\
            or event.maxstrength < 200:
        print('discarded.')
        discardedEvents += 1
        return 1

    print('accepted.')
    speed = event.getSpeedFromMaxStrength(plot=False)

    print('speed: %f direction %s' % (speed["speed"], event.getDirection()))
    return 0


if __name__ == '__main__':
    readData()
    analyzeData()
    print("total events: %d discarded events: %d" % (totalEvents, discardedEvents))
    plotData()
