import csv
import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt
import csv

xaxis = []
yaxis = []
with open('owid-covid-data-clean.csv') as data:
    csv_reader = csv.DictReader(data)
    for x in range(1,256576) :
        row = next(csv_reader)
        if row['date'] == '1/1/2023' and (row['location'] == 'Asia' or row['location'] == 'South America' or row['location'] == 'North America' or row['location'] == 'Europe' or row['location'] == 'Oceania' or row['location'] == 'Africa'):
            xaxis.append(row['population'])
            yaxis.append(row['totaldeaths'])
for i in range(0, len(yaxis)):
    yaxis[i] = int(yaxis[i])
for i in range(0, len(xaxis)):
    xaxis[i] = (int(xaxis[i]))/1000000 #This convert the population numbers from absolute numbers to millions.

plt.rcParams["figure.figsize"] = [12.00, 7.00]
plt.rcParams["figure.autolayout"] = True

plt.scatter(xaxis,yaxis, s=xaxis, alpha=0.5, color='maroon')
#Code to Add Labels of Continents
points = ['Africa','Asia','Europe','North America','Oceania','South America']
for i, txt in enumerate(points):
   plt.annotate(txt, (xaxis[i]+1.5, yaxis[i]))

#Adding the title and X and Y lable to the graph
plt.xlabel('Population (in Millions)')
plt.ylabel('Total Deaths (in Millions)')
plt.title('Total Covid-19 Cases by Population for each Continent')
plt.show() 