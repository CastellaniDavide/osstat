"""osstat
"""
import sys
import os
from datetime import datetime

__author__ = "davidecastellani@castellanidavide.it"
__version__ = "01.01 2020-04-28"

class osstat:
	def __init__ (self, directory):
		file = open("..\\log\\log.log", "a")
		start_time = datetime.now()
		osstat.log(file, f"Start time: {start_time}")
		osstat.log(file, f"Printing on screen the given directory name: {directory}")
		print(directory)

		for directories, subdirectories, files in os.walk(directory):
			osstat.log(file, f"Analizing directory {directories}")
			osstat.print_and_log(file, f"Actual directory: {directories}")
			osstat.print_and_log(file, f"Present subdirectories: {subdirectories}")
			osstat.print_and_log(file, f"Present files: {files}")
			for file_ in files:
				osstat.file_stat(file, f"{directories}\\{file_}")

		osstat.log(file, "Done")
		osstat.log(file, f"End time: {datetime.now()}\nTotal time: {datetime.now() - start_time}")
		osstat.log(file, "")
		file.close()

	def file_stat(filelog, file_path):
		"""View all proprieties for every file
		"""
		osstat.print_and_log(filelog, f"Testing file: {file_path}")
		osstat.print_and_log(filelog, os.stat(file_path))

	def log(file, item):
		"""Writes a line in the log.log file
		"""
		file.write(f"{item}\n")

	def print_and_log(file, item):
		"""Writes on the screen and in the log file
		"""
		print(item)
		osstat.log(file, item)

if __name__ == "__main__":
	try:
		osstat(sys.argv[1].replace(f'{"//"}', "\\"))
	except:
		default_directory = "..\\"
		osstat(default_directory)
