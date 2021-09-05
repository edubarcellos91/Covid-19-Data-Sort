# -*- coding: utf-8 -*-

from csv import DictReader
from tabulate import tabulate

countries = []

cases = {}
cases_per_million = {}
vaccinations = {}
people_vaccinated = {}
people_fully_vaccinated = {}
total_vaccinations_per_hundred = {}
people_vaccinated_per_hundred = {}
people_fully_vaccinated_per_hundred = {}
deaths = {}
deaths_per_million = {}

def total(key,dic):
	info = row[key]
	if not info:
		info = 0.0
	else:
		info = float(info)
	dic.append(info)

def tableOrder(dic):
	sorted_dict = dict(sorted(dic.items(),key=lambda item: item[1],reverse=True))
	sorted_countries = list(sorted_dict.keys())
	top = input('How many countries you want in the table? ')

	try:
		if int(top) > len(sorted_countries):
			top = len(sorted_countries)
		elif int(top) == 0:
			top = 1
	except Exception:
		print('Invalid value.')
		exit()

	for i in range(int(top)):
		table.append([])
		table[i].append('{}{}'.format(i+1,chr(176)))
		table[i].append(sorted_countries[i])
		table[i].append('{:,}'.format(cases[sorted_countries[i]]))
		table[i].append(cases_per_million[sorted_countries[i]])
		table[i].append('{:,}'.format(vaccinations[sorted_countries[i]]))
		table[i].append('{:,}'.format(people_vaccinated[sorted_countries[i]]))
		table[i].append('{:,}'.format(people_fully_vaccinated[sorted_countries[i]]))
		table[i].append(total_vaccinations_per_hundred[sorted_countries[i]])
		table[i].append(people_vaccinated_per_hundred[sorted_countries[i]])
		table[i].append(people_fully_vaccinated_per_hundred[sorted_countries[i]])
		table[i].append('{:,}'.format(deaths[sorted_countries[i]]))
		table[i].append(deaths_per_million[sorted_countries[i]])
	tableFinal = tabulate(table,headers,tablefmt="psql",stralign = "right",numalign="decimal",colalign=("right","left",))
	table.clear()
	print(tableFinal)

with open('owid-covid-data.csv') as csvfile:
	csv = DictReader(csvfile)
	for row in csv:
		#To discard what is not a country
		if not row['location'] in countries and row['location'] not in ['Africa','Asia','Europe','European Union','International','North America','South America','World']:
			countries.append(row['location'])
		
		casesList = []
		cases_per_millionList = []
		vacList = []
		people_vaccinatedList = []
		people_fully_vaccinatedList = []
		total_vaccinations_per_hundredList = []
		people_vaccinated_per_hundredList = []
		people_fully_vaccinated_per_hundredList = []
		deathsList = []
		deaths_per_millionList = []

		for i in range(len(countries)):
			if row['location'] == countries[i]:
				#Create lists with the data
				total('total_cases',casesList)
				total('total_cases_per_million',cases_per_millionList)
				total('total_vaccinations',vacList)
				total('people_vaccinated',people_vaccinatedList)
				total('people_fully_vaccinated',people_fully_vaccinatedList)
				total('total_vaccinations_per_hundred',total_vaccinations_per_hundredList)
				total('people_vaccinated_per_hundred',people_vaccinated_per_hundredList)
				total('people_fully_vaccinated_per_hundred',people_fully_vaccinated_per_hundredList)
				total('total_deaths',deathsList)
				total('total_deaths_per_million',deaths_per_millionList)

				#Add the bigger values to the dictionary
				cases[countries[i]] = int(max(casesList))
				cases_per_million[countries[i]] = max(cases_per_millionList)
				vaccinations[countries[i]] = int(max(vacList))
				people_vaccinated[countries[i]] = int(max(people_vaccinatedList))
				people_fully_vaccinated[countries[i]] = int(max(people_fully_vaccinatedList))
				total_vaccinations_per_hundred[countries[i]] = max(total_vaccinations_per_hundredList)
				people_vaccinated_per_hundred[countries[i]] = max(people_vaccinated_per_hundredList)
				people_fully_vaccinated_per_hundred[countries[i]] = max(people_fully_vaccinated_per_hundredList)
				deaths[countries[i]] = int(max(deathsList))
				deaths_per_million[countries[i]] = max(deaths_per_millionList)

				#Delete the lists (just yo make sure)
				casesList.clear()
				cases_per_millionList.clear()
				vacList.clear()
				people_vaccinatedList.clear()
				people_fully_vaccinatedList.clear()
				total_vaccinations_per_hundredList.clear()
				people_vaccinated_per_hundredList.clear()
				people_fully_vaccinated_per_hundredList.clear()
				deathsList.clear()
				deaths_per_millionList.clear()
			else:
				pass

print('--- Covid-19 Data Sort ---\n')
print("This software will show you a sorted list of countries' data in the order that you want.\n")
print(tabulate([['1. Total cases','6. Total vaccinations per hundred'],
				['2. Total cases per million','7. People vaccinated per hundred'],
				['3. Total vaccinations','8. People fully vaccinated per hundred'],
				['4. People vaccinated','9. Total deaths'],
				['5. People fully vaccinated','10. Total deaths per million']]))
option = input('Choose an option: ')

headers = ['Ranking','Country','Total cases','Total cases\nper million','Total\nvaccinations','People\nvaccinated',
		   'People fully\nvaccinated','Total\nvaccinations\nper hundred','People\nvaccinated\nper hundred',
		   'People fully\nvaccinated\nper hundred','Total\ndeaths','Total\ndeaths per\nmillion']
table = []

if option == '1':
	tableOrder(cases)
elif option == '2':
	tableOrder(cases_per_million)
elif option == '3':
	tableOrder(vaccinations)
elif option == '4':
	tableOrder(people_vaccinated)
elif option == '5':
	tableOrder(people_fully_vaccinated)
elif option == '6':
	tableOrder(total_vaccinations_per_hundred)
elif option == '7':
	tableOrder(people_vaccinated_per_hundred)
elif option == '8':
	tableOrder(people_fully_vaccinated_per_hundred)
elif option == '9':
	tableOrder(deaths)
elif option == '10':
	tableOrder(deaths_per_million)
else:
	print('Invalid option.')

input('Press enter to exit.')