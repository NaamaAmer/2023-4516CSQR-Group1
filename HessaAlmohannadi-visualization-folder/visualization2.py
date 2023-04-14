mydata_xaxis = []
mydata_africa = []
mydata_asia = []
mydata_europe = []
mydata_north = []
mydata_south = []
mydata_oceania = []
labels = ['Africa', 'Asia', 'Europe', 'North America', 'South America', 'Oceania']
#using a loop to read the dataset line instead of the column
with open('owid-covid-data-clean.csv', 'r') as csvfile:
    lines = csv.DictReader(csvfile)
    for x in range(1, 256576):
        row = next(lines)
        #setting conditiom for the data that will be stored in our x and y lists
        if row['continent'] == '0' and (row['location'] == 'Africa') and (
                row['date'] == '1/3/2020' or row['date'] == '1/5/2020' or row['date'] == '1/8/2020' or row[
            'date'] == '1/11/2020' or row['date'] == '1/2/2021' or row['date'] == '1/5/2021' or row[
                    'date'] == '1/8/2021' or row['date'] == '1/11/2021' or row['date'] == '1/2/2022' or row[
                    'date'] == '1/5/2022' or row['date'] == '1/8/2022' or row['date'] == '1/11/2022' or row[
                    'date'] == '1/2/2023'):
            # print(row)
            mydata_africa.append(row['total_vaccinations'])

        if row['continent'] == '0' and (row['location'] == 'Asia') and (
                row['date'] == '1/3/2020' or row['date'] == '1/5/2020' or row['date'] == '1/8/2020' or row[
            'date'] == '1/11/2020' or row['date'] == '1/2/2021' or row['date'] == '1/5/2021' or row[
                    'date'] == '1/8/2021' or row['date'] == '1/11/2021' or row['date'] == '1/2/2022' or row[
                    'date'] == '1/5/2022' or row['date'] == '1/8/2022' or row['date'] == '1/11/2022' or row[
                    'date'] == '1/2/2023'):
            mydata_xaxis.append(row['date'])
            mydata_asia.append(row['total_vaccinations'])

        if row['continent'] == '0' and (row['location'] == 'Europe') and (
                row['date'] == '1/3/2020' or row['date'] == '1/5/2020' or row['date'] == '1/8/2020' or row[
            'date'] == '1/11/2020' or row['date'] == '1/2/2021' or row['date'] == '1/5/2021' or row[
                    'date'] == '1/8/2021' or row['date'] == '1/11/2021' or row['date'] == '1/2/2022' or row[
                    'date'] == '1/5/2022' or row['date'] == '1/8/2022' or row['date'] == '1/11/2022' or row[
                    'date'] == '1/2/2023'):
            mydata_europe.append(row['total_vaccinations'])

        if row['continent'] == '0' and (row['location'] == 'North America') and (
                row['date'] == '1/3/2020' or row['date'] == '1/5/2020' or row['date'] == '1/8/2020' or row[
            'date'] == '1/11/2020' or row['date'] == '1/2/2021' or row['date'] == '1/5/2021' or row[
                    'date'] == '1/8/2021' or row['date'] == '1/11/2021' or row['date'] == '1/2/2022' or row[
                    'date'] == '1/5/2022' or row['date'] == '1/8/2022' or row['date'] == '1/11/2022' or row[
                    'date'] == '1/2/2023'):
            mydata_north.append(row['total_vaccinations'])

        if row['continent'] == '0' and (row['location'] == 'South America') and (
                row['date'] == '1/3/2020' or row['date'] == '1/5/2020' or row['date'] == '1/8/2020' or row[
            'date'] == '1/11/2020' or row['date'] == '1/2/2021' or row['date'] == '1/5/2021' or row[
                    'date'] == '1/8/2021' or row['date'] == '1/11/2021' or row['date'] == '1/2/2022' or row[
                    'date'] == '1/5/2022' or row['date'] == '1/8/2022' or row['date'] == '1/11/2022' or row[
                    'date'] == '1/2/2023'):
            mydata_south.append(row['total_vaccinations'])

        if row['continent'] == '0' and (row['location'] == 'Oceania') and (
                row['date'] == '1/3/2020' or row['date'] == '1/5/2020' or row['date'] == '1/8/2020' or row[
            'date'] == '1/11/2020' or row['date'] == '1/2/2021' or row['date'] == '1/5/2021' or row[
                    'date'] == '1/8/2021' or row['date'] == '1/11/2021' or row['date'] == '1/2/2022' or row[
                    'date'] == '1/5/2022' or row['date'] == '1/8/2022' or row['date'] == '1/11/2022' or row[
                    'date'] == '1/2/2023'):
            mydata_oceania.append(row['total_vaccinations'])
#using a for loop to convert our y axis variables from string to integers so they may display correctly on our graph
for i in range(0, len(mydata_africa)):
    mydata_africa[i] = (int(mydata_africa[i])) / 1000000000
for i in range(0, len(mydata_south)):
    mydata_south[i] = (int(mydata_south[i])) / 1000000000
for i in range(0, len(mydata_oceania)):
    mydata_oceania[i] = (int(mydata_oceania[i])) / 1000000000
for i in range(0, len(mydata_asia)):
    mydata_asia[i] = (int(mydata_asia[i])) / 1000000000
for i in range(0, len(mydata_europe)):
    mydata_europe[i] = (int(mydata_europe[i])) / 1000000000
for i in range(0, len(mydata_north)):
    mydata_north[i] = (int(mydata_north[i])) / 1000000000
#definig the size of the graph
plt.rcParams["figure.figsize"] = [12.00, 7.00]
plt.rcParams["figure.autolayout"] = True
# it represents the type of the graph
plt.stackplot(mydata_xaxis, mydata_africa, mydata_asia, mydata_europe, mydata_north, mydata_south, mydata_oceania,
              labels=labels)
#adding labels and a title
plt.xlabel('Date')
plt.ylabel('Total vaccinations administered (in Billions)')
plt.title('Total Vaccinations Administered Over Time by Continent', fontsize=20)
plt.legend(loc=(.07, .75))
#displaying a   graph
plt.show()
