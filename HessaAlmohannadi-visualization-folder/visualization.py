visualization
import matplotlib.pyplot as plt
import csv
#Create list for the x and y to carry our variables
mydata_xaxis = []
mydata_yaxis = []
#using a loop to read the dataset line by line
with open('owid-covid-data-clean.csv', 'r') as csvfile:
    lines = csv.DictReader(csvfile)
    for x in range(1,256576):
        row = next(lines)
        #putting actions for the data that will be stored in our x and y lists
        if row['date'] == '1/1/2023':
            print(row)
            mydata_xaxis.append(row['human_development_index'])
            for i in range(0, len(mydata_xaxis)):
                mydata_xaxis[i] = float(mydata_xaxis[i])
#using a for loop to  convert our y axis variable from a string to integer for them to be represented apropriatly on the graph
            mydata_yaxis.append(row['totaldeathspermillion'])
            for j in range(0, len(mydata_yaxis)):
                mydata_yaxis[j] = float(mydata_yaxis[j])
#identifing the type of graph
plt.scatter(mydata_xaxis,mydata_yaxis)
#inserting a title for the graph
plt.xlabel('Human Development Index')
plt.ylabel('Total Death per million')
plt.title('Total death per million in the Year 2023', fontsize=20)
#plt.fill_between(mydata_xaxis,mydata_yaxis)
plt.show()