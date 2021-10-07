import json
import csv

f = open('covid_cases.json')
data = json.load(f)

dateReported = []
countriesTerritories = []
numberCases = []
numberDeaths = []

newColumns = ["Date Reported", "Countries and Territories", "Number of Cases", "Number of Deaths"]

for reported in data['records']:
    dateReported.append(reported['dateRep'])

for countriesTerror in data['records']:
    countriesTerritories.append(countriesTerror['countriesAndTerritories'])

for Cases in data['records']:
    numberCases.append(Cases['cases'])

for Deaths in data['records']:
    numberDeaths.append(Deaths['deaths'])

#Creating a CSV 
#Knowing the length of dataset.

length = len(dateReported)

with open("NewData.csv", newline="", mode="w") as csvGenerator:
    covid_csv = csv.writer(csvGenerator)
    covid_csv.writerow(newColumns)

    for newData in range(length): #the value of length is 6540
        row = [dateReported[newData],countriesTerritories[newData],numberCases[newData],numberDeaths[newData]]
        covid_csv.writerow(row)


f.close()