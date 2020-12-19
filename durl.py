#! /usr/bin/env python3
# durl.py - Download provided url file.
# python durl.py <url>

import requests
import os
import subprocess
import sys
from pathlib import Path
import shutil
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)

if len(sys.argv) > 1:
	foldername = Path('stuff')
	os.makedirs(foldername, exist_ok=True)

	urls = [url if url.startswith('https://') else 'https://' + url for url in sys.argv[1:]]

	# Deal with shell placing backslashes '\' in urls when wrapping argument in quotes.
	urls = [url.replace('\\', '') for url in urls]

	for url in urls:
		res = requests.get(url)
		res.raise_for_status()
		
		filename = Path(url).name	
		print(f'Downloading {url}...')

		with open(foldername / filename, 'wb') as f:
			for chunk in res.iter_content(chunk_size=1024*1024):
				if chunk:
					f.write(chunk)
		
		# Rename file if it doesn't have the format
		file_info = str(subprocess.Popen(['file', str(foldername/filename)], stdout=subprocess.PIPE).communicate()[0])

		file_format = file_info.split()[1].lower()

		if not filename.endswith(file_format):
			file_path = str(foldername / filename)
			new_file_path = file_path + '.' + file_format 
			shutil.move(file_path, new_file_path)
else:
	print('Invalid command.')
	print(f'Try: python {__file__} <urls>')

