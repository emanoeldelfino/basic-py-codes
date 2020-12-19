#! python3
# rename_files.py - Rename files to lowercase and replace spaces with underscores.
# py.exe rename_files.py

import shutil
import os
import time

files = os.listdir('.')

new_files = [file.lower().replace(' ', '_') for file in files]

abs_working_dir = os.path.abspath('.')

for old_filename, new_filename in zip(files, new_files):
	abs_old_filename = os.path.join(abs_working_dir, old_filename)

	print(f'Renaming "{old_filename}" to "{new_filename}"')	

	time.sleep(2)

	shutil.move(old_filename, new_filename)

