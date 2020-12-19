import requests

image_url = "https://www.python.org/static/img/python-logo.png"

r = requests.get(image_url)

with open('python-logo.png', 'wb') as f:
	f.write(r.content)

