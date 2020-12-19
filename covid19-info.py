import requests
import bs4
import sys

if len(sys.argv) == 2:
	country = sys.argv[1]
	
	url = f'https://www.worldometers.info/coronavirus/country/{country}'
	r = requests.get(url)
	soap = bs4.BeautifulSoup(r.text, 'html.parser')
	
	last_update = soap.select("div[class='label-counter'] + div")[0].getText()

	cases, deaths, recovered = [elem.getText() for elem in soap.select("div[class='maincounter-number'] span")]

	active_cases, closed_cases = [elem.getText() for elem in soap.select("div[class='number-table-main']")]
	
	mild, serious = [elem.getText() for elem in soap.select("span[class='number-table']")[:2]]

	percents = [elem.getText() for elem in soap.select("span[class='number-table'] + strong")]

	mild_per, serious_per, rec_per, death_per = percents

	print(last_update)
	print()
	print(f'Cases: {cases}')
	print()
	print(f'Active cases: {active_cases}')
	print(f'Mild cases: {mild} - {mild_per}%')
	print(f'Serious cases: {serious} - {serious_per}%')
	print()	
	print(f'Closed cases: {closed_cases}')
	print(f'Recovered: {recovered} - {rec_per}%')
	print(f'Death: {deaths} - {death_per}%')
else:
	print('Invalid command.')
	print(f'Try: python {__file__} <country>')


