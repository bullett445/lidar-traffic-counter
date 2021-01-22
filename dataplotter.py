import csv
import matplotlib.pyplot as plt
import array

def plotData():
    firsttimestamp = 0
    timestamps = array.array('d')
    distances = array.array('f')
    strength = array.array('i')
    with open('data/front_twolanes_30kmh.csv') as f:
        reader = csv.reader(f, delimiter=';')
        for line in reader:
            if firsttimestamp == 0:
                firsttimestamp = float(line[0])
            timestamps.append(float(line[0]) - firsttimestamp)
            distances.append(int(line[1]) / 100)
            strength.append(int(line[2]))
    plt.scatter(timestamps, distances, c=strength);
    plt.xlabel('wallclock since start [seconds]')
    plt.ylabel('distance [m]')
    clb = plt.colorbar()
    clb.ax.set_title('strength')
    plt.show();

if __name__ == '__main__':
    plotData()
