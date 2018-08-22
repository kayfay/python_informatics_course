import os
import csv
from pylab import arange, bar, xticks, ylabel, title, figure, gca, plot
from pylab import xlabel, grid, axis, show, legend

# Initialize Variables
NMI = 1852.0
xData = []
xLabels = []
names = []
lats = []
longs = []
vels = []
secs = []
gpsCommands = {}


def readCSVFile(filename):
    """
    Returns a list file containing strings of colulmns from a csv

    args: csv file
    returns: list of strings
    """
    data = []
    file = open(filename)
    csvfile = csv.reader(file)
    for row in csvfile:
        data.append(row)
    file.close()
    return data


def listGPSCommands(data):
    """
    Takes a list of strings and checks for a value then generates a dictionary
    of GPS commands and their frequency

    args: list data with GPS commands at index 0
    returns: dictionary {GPS Command : occurances}
    """
    gps_cmds = dict()
    for row in data:
        try:
            gps_cmds[row[0]] += 1
        except KeyError:
            gps_cmds[row[0]] = 1
    return gps_cmds


def processGPSData(data):
    """
    Uses python list comprehension to call four functions and return lists.

    arg: a data infile
    returns: a latitude, longitude, velocity, seconds, and frequency list
    """
    latitude = []
    longitude = []
    velocity = []
    seconds = []
    frequency = 0

    latitude.append(getLatitudeFromGPS(data))
    longitude.append(getLongitudeFromGPS(data))
    velocity.append(gpsVelocity(data))
    seconds.append(tSeconds(data))
    frequency += gpsFrequency(data)

    return [x for x in [latitude, longitude, velocity, seconds, frequency]]


def tSeconds(data):
    """
    A function to pull the seconds from NMEA 0183 Standard GPS csv
    specfic to the  RMC recommended minimum data for gps

    args: a list of the csv data
    returns: a list of seconds
    """
    return [
        float(row[1][0:2]) * 3600 + float(row[1][2:4]) * 60 +
        float(row[1][4:6]) for row in data if row[0] == '$GPRMC'
    ]


def gpsFrequency(data):
    """
    A function to pull the frequencies from NMEA 0183 Standard GPS csv
    specfic to the GSV Overall Satellite data

    args: a list of the csv data
    returns: the total frequency of entiries
    """
    return len([row for row in data if row[0] == '$GPGSV'])


def getLatitudeFromGPS(data):
    """
    A function to pull the latitude from NMEA 0183 Standard GPS csv
    specfic to the  RMC recommended minimum data for gps

    args: a list of the csv data
    returns: a list of latitude entires
    """
    return [
        float(row[3][0:2]) + float(row[3][2:]) / 60.0 for row in data
        if row[0] == '$GPRMC'
    ]


def getLongitudeFromGPS(data):
    """
    A function to pull the longitude from NMEA 0183 Standard GPS csv
    specfic to the  RMC recommended minimum data for gps

    args: a list of the csv data
    returns: a list of longitude entires
    """
    return [
        float(row[5][0:3]) + float(row[5][3:]) / 60.0 for row in data
        if row[0] == '$GPRMC'
    ]


def gpsVelocity(data):
    """
    A function to pull the velocity from NMEA 0183 Standard GPS csv
    specfic to the  RMC recommended minimum data for gps

    args: a list of the csv data
    returns: a list of velocity entries
    """
    return [float(row[7]) * NMI / 1000.0 for row in data if row[0] == '$GPRMC']


# ==== Main ====
# Process files in data directory
for root, dirs, files in os.walk('../data'):
    for filename in files:
        # Create the full (absolute) path for each file
        curFile = os.path.join(root, filename)
        if (filename.endswith('csv')):
            names.append(curFile)  # Enumerate a list of file names

# Create lists for travel
for curFile in names:
    # Create an data for each file
    filecontents = readCSVFile(curFile)
    # Create a list of ['cmd', 'freq']
    gpsCommands.update(listGPSCommands(filecontents))
    # enumerate lists from gps data
    (latitude, longitude, velocity, seconds,
     frequency) = processGPSData(filecontents)
    lats.extend(latitude)
    longs.extend(longitude)
    vels.extend(velocity)
    secs.extend(seconds)

lats = lats[1]
longs = longs[1]

# === Display a frequency table
print("Command Frequency")
print("======= =========")
# iteration, gpsCommands contains
# {'gpscmd':occurances, 'gpscmd2':occurances, ...}
for command in gpsCommands:
    print(command, '  ', gpsCommands[command])
    xLabels.append(command)
    xData.append(gpsCommands[command])

# ==== Bar Graph of Commands and Frequency ====

bars = arange(len(xData))
bar(bars, xData, align='center')
xticks(bars, xLabels, rotation=-10)
ylabel("Number of Unique Commands")
title('Unique GPS Commands Found in File')
figure()

# ==== Plots of GPS locations ====
gca().axes.invert_xaxis()
plot(longs, lats, 'b', label='Crusing', linewidth=3)
title(names[0][8:-11] + ' ' + names[1][8:-11])
legend(loc='upper left')
xlabel('East-West (meters)')
ylabel('South-North (meters)')
grid()
axis('equal')
figure()

print("The number of records in the file is ", len(filecontents))
print("The average speed was", round(sum(vels[0]) / len(vels[0])), "units")

show()
