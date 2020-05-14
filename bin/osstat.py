"""osstat
"""
import sys
import os
from datetime import datetime
from urllib.request import urlopen
from bs4 import BeautifulSoup

__author__ = "davidecastellani@castellanidavide.it"
__version__ = "01.03 2020-05-05"

class osstat:
	def __init__ (self, directory, vs=False):
		"""Inizialiting files, scan the files and ends the program
		"""
		base_dir = "castellani_davide_osstat_01_03" if vs else ".." # the project "root" in Visual studio it is different

		file = open(os.path.join(base_dir, "log", "log.log"), "a")
		csv_file = os.path.join(base_dir, "flussi", "osstat.csv")

		start_time = datetime.now()

		osstat.log(file, f"Start time: {start_time}")
		osstat.log(file, "Inizializing the csv file")
		osstat.csv_setup(csv_file)
		osstat.log(file, f"Printing on screen the given directory name: {directory}")
		print(directory)

		for directories, subdirectories, files in os.walk(directory):
			osstat.log(file, f"Analizing directory {directories}")
			osstat.print_and_log(file, f"Actual directory: {directories}")
			osstat.print_and_log(file, f"Present subdirectories: {subdirectories}")
			osstat.print_and_log(file, f"Present files: {files}")
			for file_ in files:
				osstat.file_stat(file, os.path.join(directories, file_), csv_file)

		osstat.log(file, "Done")
		osstat.log(file, f"End time: {datetime.now()}\nTotal time: {datetime.now() - start_time}")
		osstat.log(file, "")
		file.close()

	def file_stat(filelog, file_path, filecsv):
		"""View all proprieties for every file
		"""
		osstat.print_and_log(filelog, f"Testing file: {file_path}")
		osstat.csv_write(filelog, filecsv, f"{file_path},{os.stat(file_path).st_mode},{os.stat(file_path).st_ino},{os.stat(file_path).st_dev},{os.stat(file_path).st_nlink},{os.stat(file_path).st_uid},{os.stat(file_path).st_gid},{os.stat(file_path).st_size},{os.stat(file_path).st_atime},{osstat.time_converter(os.stat(file_path).st_atime)},{os.stat(file_path).st_mtime},{osstat.time_converter(os.stat(file_path).st_mtime)},{os.stat(file_path).st_ctime},{osstat.time_converter(os.stat(file_path).st_ctime)}")

	def log(file, item):
		"""Writes a line in the log.log file
		"""
		print(item)
		file.write(f"{item}\n")

	def print_and_log(file, item):
		"""Writes on the screen and in the log file
		"""
		print(item)
		osstat.log(file, item)

	def csv_setup(file_csv):
		"""Write the intestation of the csv file
		"""
		with open(file_csv, "w+") as csv:
			csv.write("filename, st_mode,st_ino,st_dev,st_nlink,st_uid,st_gid,st_size,st_atime,st_atime for humans,st_mtime,st_mtime for humans,st_ctime,st_ctime for humans\n")

	def csv_write(file_log, file_csv, item):
		"""Writes on the csv file, screen and in the log file
		"""
		osstat.print_and_log(file_log, f"Write on csv file {item}")
		with open(file_csv, "a") as csv:
			csv.write(f"{item}\n")

	def time_converter(unix):
		"""Return my time by UNIX to user friendly one
		"""
		url = f'https://showcase.linx.twenty57.net:8081/UnixTime/fromunix?timestamp={int(unix)}' #  my WebService
		return urlopen(url).read()

if __name__ == "__main__":
	# degub flag
	debug = False

	# My call
	try:
		osstat(sys.argv[1], debug)
	except:
		default_directory = "castellani_davide_osstat_01_03" if debug else".."
		osstat(default_directory, debug)
