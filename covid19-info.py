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

	cases = [elem.getText() for elem in soap.select("div[class='number-table-main']")]

	if len(cases) == 2:
		active_cases, closed_cases = cases
	elif len(cases) == 1:
		active_cases, closed_cases = [0] + cases

	mild, serious = [elem.getText() for elem in soap.select("span[class='number-table']")[:2]]

	percents = [elem.getText() for elem in soap.select("span[class='number-table'] + strong")]

	if len(percents) == 4:
		mild_per, serious_per, rec_per, death_per = percents
	elif len(percents) == 2:
		mild_per, serious_per = [0, 0]
		rec_per, death_per = percents

	print(last_update)
	print()
	print(f'Cases: ', end='')
	for case in cases:
		print(case, end=' ')
	print()

	if active_cases:
		print(f'Active cases: {active_cases}')

	if mild_per or serious_per:
		print(f'Mild cases: {mild} - {mild_per}%')
		print(f'Serious cases: {serious} - {serious_per}%')
		print()

	print(f'Closed cases: {closed_cases}')
	print(f'Recovered: {recovered} - {rec_per}%')
	print(f'Death: {deaths} - {death_per}%')
else:
	print('Invalid command.')
	print(f'Try: python {__file__} <country>')
