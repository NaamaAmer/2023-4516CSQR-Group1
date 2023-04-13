import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv


#Total Cases By Continent Bar Graph

#Create lists for the x and y axis to carry our variables
mydata_xaxis = []
mydata_yaxis = []
#Opening the dataset and using a loop to read the dataset line by line instead of by column
with open('owid-covid-data-clean.csv') as data:
    csv_reader = csv.DictReader(data)
    for x in range(1,256576) :
        row = next(csv_reader)
        #Setting conditions for the data that will be stored in our x and y lists
        if row['date'] == '1/1/2023' and row['continent'] == '0' and (row['location'] == 'World' or row['location'] == 'Asia' or row['location'] == 'South America' or row['location'] == 'North America' or row['location'] == 'Europe' or row['location'] == 'Oceania' or row['location'] == 'Africa'):
            #Using the print function to test if the data selected is correct
            #print(row)
            #Appending the filtered data to our y and x lists
            mydata_xaxis.append(row['location'])
            mydata_yaxis.append(row['totalcases'])
#Using a for loop to convert our y axis variables from string to integer so they may be displayed correctly on our graph
for i in range(0, len(mydata_yaxis)):
    mydata_yaxis[i] = (int(mydata_yaxis[i]))/1000000

#Plotting a bar chart with the x and y lists
plt.barh(mydata_xaxis,mydata_yaxis)
#Adding labels and a title
plt.xlabel('Total Cases (in Millions)')
plt.title('Total Covid-19 Cases by Continent')
#Displaying the graph
plt.show()






#Total Cases Overtime from Beginning of Pandemic to 1/2/2023 Worldwide

#Create lists for the x and y axis to carry our variables
mydata_xaxis = []
mydata_yaxis = []
#Opening the dataset and using a loop to read the dataset line by line instead of by column
with open('owid-covid-data-clean.csv') as data:
    csv_reader = csv.DictReader(data)
    for x in range(1,256576) :
        row = next(csv_reader)
        #Setting conditions for the data that will be stored in our x and y lists
        if row['continent'] == '0' and row['location'] == 'World' and (row['date'] == '1/2/2020' or row['date'] == '1/5/2020' or row['date'] == '1/8/2020' or row['date'] == '1/11/2020' or row['date'] == '1/2/2021' or row['date'] == '1/5/2021' or row['date'] == '1/8/2021' or row['date'] == '1/11/2021' or row['date'] == '1/2/2022' or row['date'] == '1/5/2022' or row['date'] == '1/8/2022' or row['date'] == '1/11/2022' or row['date'] == '1/2/2023'):
            #Using the print function to test if the data selected is correct
            #print(row)
            #Appending the filtered data to our y and x lists
            mydata_xaxis.append(row['date'])
            mydata_yaxis.append(row['totalcases'])
            #Using a for loop to convert our y axis variables from string to integer so they may be displayed correctly on our graph
            for i in range(0, len(mydata_yaxis)):
                mydata_yaxis[i] = int(mydata_yaxis[i])

#Specifying the size of the graph
plt.rcParams["figure.figsize"] = [12.00, 7.00]
plt.rcParams["figure.autolayout"] = True

#Plotting a line graph using our x and y variables
plt.plot(mydata_xaxis, mydata_yaxis)
#Adding a title and labels
plt.title('Number of Covid-19 Cases Worldwide from the Beginning of the Pandemic to 1/2/2023')
plt.ylabel('Total Cases (in 100 Millions)')
plt.xlabel('Date')
#Filling the space between the line and the bottom of the graph to create an area chart
plt.fill_between(mydata_xaxis, mydata_yaxis)
#Displaying the Graph
plt.show()






#Stackplot of the Total Cases Over Time for Each Continent from 1/3/2020 to 1/2/2023 (Hajar)

#Create lists for the x axis and continents to carry our variables
mydata_xaxis = []
mydata_africa = []
mydata_asia = []
mydata_europe = []
mydata_north = []
mydata_south = []
mydata_oceania = []
#Create list for the labels we will use in our legend
labels = ['Africa', 'Asia', 'Europe', 'North America', 'South America', 'Oceania']
#Opening the dataset and using a loop to read the dataset line by line instead of by column
with open('owid-covid-data-clean.csv') as data:
    csv_reader = csv.DictReader(data)
    for x in range(1,256576) :
        row = next(csv_reader)
        #For each continent and the x axis we set conditions for the data that will be stored in our lists,
        #Then we appended the filtered data to our lists
        #Then used a for loop to convert our continent variables from string to integer so they may be displayed correctly on our graph
        if row['continent'] == '0' and (row['location'] == 'Africa') and (row['date'] == '1/3/2020' or row['date'] == '1/5/2020' or row['date'] == '1/8/2020' or row['date'] == '1/11/2020' or row['date'] == '1/2/2021' or row['date'] == '1/5/2021' or row['date'] == '1/8/2021' or row['date'] == '1/11/2021' or row['date'] == '1/2/2022' or row['date'] == '1/5/2022' or row['date'] == '1/8/2022' or row['date'] == '1/11/2022' or row['date'] == '1/2/2023'):
            #print(row)
            #We used the print function to test if each row produced the correct filtered data
            mydata_africa.append(row['totalcases'])
            for i in range(0, len(mydata_africa)):
                mydata_africa[i] = int(mydata_africa[i])
        if row['continent'] == '0' and (row['location'] == 'Asia') and (row['date'] == '1/3/2020' or row['date'] == '1/5/2020' or row['date'] == '1/8/2020' or row['date'] == '1/11/2020' or row['date'] == '1/2/2021' or row['date'] == '1/5/2021' or row['date'] == '1/8/2021' or row['date'] == '1/11/2021' or row['date'] == '1/2/2022' or row['date'] == '1/5/2022' or row['date'] == '1/8/2022' or row['date'] == '1/11/2022' or row['date'] == '1/2/2023'):
            mydata_xaxis.append(row['date'])
            mydata_asia.append(row['totalcases'])
            for i in range(0, len(mydata_asia)):
                mydata_asia[i] = int(mydata_asia[i])
        if row['continent'] == '0' and (row['location'] == 'Europe') and (row['date'] == '1/3/2020' or row['date'] == '1/5/2020' or row['date'] == '1/8/2020' or row['date'] == '1/11/2020' or row['date'] == '1/2/2021' or row['date'] == '1/5/2021' or row['date'] == '1/8/2021' or row['date'] == '1/11/2021' or row['date'] == '1/2/2022' or row['date'] == '1/5/2022' or row['date'] == '1/8/2022' or row['date'] == '1/11/2022' or row['date'] == '1/2/2023'):
            mydata_europe.append(row['totalcases'])
            for i in range(0, len(mydata_europe)):
                mydata_europe[i] = int(mydata_europe[i])
        if row['continent'] == '0' and (row['location'] == 'North America') and (row['date'] == '1/3/2020' or row['date'] == '1/5/2020' or row['date'] == '1/8/2020' or row['date'] == '1/11/2020' or row['date'] == '1/2/2021' or row['date'] == '1/5/2021' or row['date'] == '1/8/2021' or row['date'] == '1/11/2021' or row['date'] == '1/2/2022' or row['date'] == '1/5/2022' or row['date'] == '1/8/2022' or row['date'] == '1/11/2022' or row['date'] == '1/2/2023'):
            mydata_north.append(row['totalcases'])
            for i in range(0, len(mydata_north)):
                mydata_north[i] = int(mydata_north[i])
        if row['continent'] == '0' and (row['location'] == 'South America') and (row['date'] == '1/3/2020' or row['date'] == '1/5/2020' or row['date'] == '1/8/2020' or row['date'] == '1/11/2020' or row['date'] == '1/2/2021' or row['date'] == '1/5/2021' or row['date'] == '1/8/2021' or row['date'] == '1/11/2021' or row['date'] == '1/2/2022' or row['date'] == '1/5/2022' or row['date'] == '1/8/2022' or row['date'] == '1/11/2022' or row['date'] == '1/2/2023'):
            mydata_south.append(row['totalcases'])
            for i in range(0, len(mydata_south)):
                mydata_south[i] = int(mydata_south[i])
        if row['continent'] == '0' and (row['location'] == 'Oceania') and (row['date'] == '1/3/2020' or row['date'] == '1/5/2020' or row['date'] == '1/8/2020' or row['date'] == '1/11/2020' or row['date'] == '1/2/2021' or row['date'] == '1/5/2021' or row['date'] == '1/8/2021' or row['date'] == '1/11/2021' or row['date'] == '1/2/2022' or row['date'] == '1/5/2022' or row['date'] == '1/8/2022' or row['date'] == '1/11/2022' or row['date'] == '1/2/2023'):
            mydata_oceania.append(row['totalcases'])
            for i in range(0, len(mydata_oceania)):
                mydata_oceania[i] = int(mydata_oceania[i])

#Specifying the size of the graph
plt.rcParams["figure.figsize"] = [12.00, 7.00]
plt.rcParams["figure.autolayout"] = True

#Plotting a stackplot with the x axis and the continent as the y axis and the labels are the labels list
plt.stackplot(mydata_xaxis, mydata_africa, mydata_asia, mydata_europe, mydata_north, mydata_south, mydata_oceania, labels = labels)
#Adding a title and x and y axis labels
plt.title('Number of Covid-19 Cases by Continent from the (1/3/2020) till (1/2/2023)')
plt.ylabel('Total Cases (in 100 Millions)')
plt.xlabel('Date')
#Adding a legend
plt.legend(loc=(.07, .75))
#Displaying the graph
plt.show()