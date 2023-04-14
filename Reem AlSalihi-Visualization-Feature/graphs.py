import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv

#Create lists for the x and y axis to carry our variables
mydata_xaxis = []
mydata_yaxis = []
#Opening the dataset and using a loop to read the dataset line by line instead of by column
with open('owid-covid-data-clean.csv') as data:
    csv_reader = csv.DictReader(data)
    for x in range(1,256576) :
        row = next(csv_reader)
        #Setting conditions for the data that will be stored in our x and y lists
        if row['date'] == '1/1/2023' and (row['location'] == 'Asia' or row['location'] == 'South America' or row['location'] == 'North America' or row['location'] == 'Europe' or row['location'] == 'Oceania' or row['location'] == 'Africa'):
              #print(row)
              #Appending the filtered data to our y and x lists
            mydata_xaxis.append(row['location'])
            mydata_yaxis.append(row['totalcases'])

#plt.pie will plot the piechart using the x and y axis we had, autopct is where the percentage shows on each slice
#startangle is for what angle each pie should start at
plt.pie(mydata_yaxis, labels=mydata_xaxis, autopct='%1.1f%%', startangle=90)
plt.title('Total Covid-19 Cases for each Continent') #the title of the graph
plt.show() #display graph

#second graph

#Create lists for the x and y axis to carry our variables
mydata_xaxis = []
mydata_yaxis = []
#Opening the dataset and using a loop to read the dataset line by line instead of by column
with open('owid-covid-data-clean.csv') as data:
    csv_reader = csv.DictReader(data)
    for x in range(1, 256576):
        row = next(csv_reader)
        #Setting conditions for the data that will be stored in our x and y lists
        if row['date'] == '1/1/2023' and row['continent'] == '0' and (row['location'] == 'Asia' or row['location'] == 'South America' or row['location'] == 'North America' or row['location'] == 'Europe' or row['location'] == 'Oceania' or row['location'] == 'Africa'):
           #Appending the filtered data to our y and x lists
            mydata_xaxis.append(row['location'])
            mydata_yaxis.append(float(row['totalcasespermillion'])) #takes it as a float as it decimals 

plt.rcParams["figure.figsize"] = [12.00, 7.00] #sets the size of the figure to be 12 inches wide and 7 inches high.
plt.rcParams["figure.autolayout"] = True #s a setting that automatically adjusts the spacing between the subplots to fit the contents of the figure. It can help prevent overlapping of labels, titles, and other elements in the figure

#plots the bar graph according to my x and y axis
plt.bar(mydata_xaxis, mydata_yaxis)
#graph labels and title
plt.title('Total Covid-19 Cases per Million by Continent')
plt.xlabel('Continent')
plt.ylabel('Total Covid-19 Cases per Million')
plt.show() #display the graph