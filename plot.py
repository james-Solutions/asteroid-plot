#!/usr/bin/env sage
import sys
import csv
from sage.all import *

'''
This script pulls in Asteroid data from a local csv file. It initially reads in all
the data into a list of asteroids. While reading in checking for min and max for both
year and velocity. Then a graph is produced with axes based on these min and maxes.
The first graph is a Miss in AU vs Year plot, showchasing all the asteroids in the data.
The second is a Miss in AU vs Velocity plot. In which the data is broken into 4 groups from;
min - 1/4 of max
1/4 - 1/2 of max
1/2 - 3/4 of max
3/4 - max
Mostly this is to make the data more meaningful in the graph by changing each different
groupings face color. Finally the script saves the 2 plots to the local directory.
'''

class Asteroid:
  def __init__(self, year, missInAU, velocity):
    self.year = year
    self.missInAU = missInAU
    self.velocity = velocity

def shortBubbleSort(list):
  exchanges = True
  passnum = len(list)-1
  while passnum > 0 and exchanges:
    exchanges = False
    for i in range(passnum):
      currentVel = float(list[i].velocity)
      nextVel = float(list[i+1].velocity)
      if currentVel < nextVel:
        exchanges = True
        temp = list[i]
        list[i] = list[i+1]
        list[i+1] = temp
    passnum = passnum - 1

file = open('data.csv')
data = csv.reader(file)
firstRow = next(data)
file.seek(0)
distancePlot = Graphics()
velocityPlot = Graphics()

asteroids = []
maxYear = 0
minYear = firstRow[2]
minVel = float(firstRow[10])
maxVel = float(0.0)
# iterate the csv file
for row in data:
  '''
  row[2] = year
  row[9] = miss in au
  row[10] = vel in km/s
  '''
  currentVel = float(row[10])
  currentYear = int(row[2])
  if currentVel > maxVel:
    maxVel = currentVel
  elif currentVel < minVel:
    minVel = currentVel
  if currentYear > maxYear:
    maxYear = currentYear
  elif currentYear < minYear:
    minYear = currentYear
  readAsteroid = Asteroid(row[2], row[9], row[10])
  asteroids.append(readAsteroid)

threeQuarterVel = float(float(maxVel) / float(1.0 / 0.75))
halfVel = float(maxVel / 2.0)
quarterVel = float(float(maxVel) / float(1.0 / 0.25))

underQuarterAsteroids = []
quarterToHalfAsteroids = []
halfToThreeQuarterAsteroids = []
threeQuarterToMaxAsteroids = []

firstVelPlot = []
secondVelPlot = []
thirdVelPlot = []
fourthVelPlot = []
distanceDataPlot = []

for data in asteroids:
  currentVel = float(data.velocity)
  if currentVel < quarterVel:
    underQuarterAsteroids.append(data)
  elif currentVel < halfVel:
    quarterToHalfAsteroids.append(data)
  elif currentVel < threeQuarterVel:
    halfToThreeQuarterAsteroids.append(data)
  elif currentVel <= maxVel:
    threeQuarterToMaxAsteroids.append(data)


print "Max Vel: ", maxVel
print "Min Vel: ", minVel
print "3/4 Vel: ", threeQuarterVel
print "1/2 Vel: ", halfVel
print "1/4 Vel: ", quarterVel
print "< 1/4 VEL ASTEROIDS"
print "Total: ", len(underQuarterAsteroids)
for data in underQuarterAsteroids:
  firstVelPlot.append(tuple((data.velocity, data.missInAU)))
  distanceDataPlot.append(tuple((data.year, data.missInAU)))
  print("Year: " + data.year + ", Miss in AU: " + data.missInAU + ", Veloctiy (km/s): " + data.velocity)


print "1/4 - 1/2 ASTEROIDS"
print "Total: ", len(quarterToHalfAsteroids)
for data in quarterToHalfAsteroids:
  secondVelPlot.append(tuple((data.velocity, data.missInAU)))
  distanceDataPlot.append(tuple((data.year, data.missInAU)))
  print("Year: " + data.year + ", Miss in AU: " + data.missInAU + ", Veloctiy (km/s): " + data.velocity)

print "1/2 - 3/4 ASTEROIDS"
print "Total: ", len(halfToThreeQuarterAsteroids)
for data in halfToThreeQuarterAsteroids:
  thirdVelPlot.append(tuple((data.velocity, data.missInAU)))
  distanceDataPlot.append(tuple((data.year, data.missInAU)))
  print("Year: " + data.year + ", Miss in AU: " + data.missInAU + ", Veloctiy (km/s): " + data.velocity)

print "3/4 - Max ASTEROIDS"
print "Total: ", len(threeQuarterToMaxAsteroids)
for data in threeQuarterToMaxAsteroids:
  fourthVelPlot.append(tuple((data.velocity, data.missInAU)))
  distanceDataPlot.append(tuple((data.year, data.missInAU)))
  print("Year: " + data.year + ", Miss in AU: " + data.missInAU + ", Veloctiy (km/s): " + data.velocity)

print "Total Asteroids: ", (len(underQuarterAsteroids) + len(quarterToHalfAsteroids) + len(halfToThreeQuarterAsteroids) + len(threeQuarterToMaxAsteroids))



# then make the scatter plot
distanceVsYear = scatter_plot(distanceDataPlot)
quarterVelocityPlot = scatter_plot(firstVelPlot, facecolor='green')
quarterToHalfVelocityPlot = scatter_plot(secondVelPlot, facecolor='blue')
halfToThreeQuarterVelocityPlot = scatter_plot(thirdVelPlot, facecolor='purple')
threeQuarterToMaxVelocityPlot = scatter_plot(fourthVelPlot, facecolor='red')

distancePlot += distanceVsYear
velocityPlot += quarterVelocityPlot + quarterToHalfVelocityPlot + halfToThreeQuarterVelocityPlot + threeQuarterToMaxVelocityPlot

distancePlot.set_axes_range(minYear, maxYear, 0, 0.2)
distancePlot.axes_labels(['Year(s)', 'Miss in AU'])
velocityPlot.set_axes_range(minVel, maxVel, 0, 0.2)
velocityPlot.axes_labels(['Velocity (km/s)', 'Miss in AU'])

distancePlot.save('distance-plot.png')
velocityPlot.save('velocity-plot.png')