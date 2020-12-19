import requests

urls = ['https://github.githubassets.com/favicons/favicon.png', 
	'https://github.githubassets.com/favicons/favicon.svg']

filenames = ['gh_favicon.png', 'gh_favicon.svg']

for url, filename in zip(urls, filenames):
	response = requests.get(url)

	with open(filename, 'wb') as f:
		f.write(response.content)

