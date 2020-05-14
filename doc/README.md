# osstat
![Author](https://img.shields.io/badge/author-Castellani%20Davide-green?style=flat)
![Version](https://img.shields.io/badge/version-v02.01-blue?style=flat)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/CastellaniDavide/osstat?label=lastest%20relase)
![Language vbs](https://img.shields.io/badge/language-Python3-yellowgreen?style=flat)
![sys.platform supported](https://img.shields.io/badge/os%20platform%20supported-Windows%2010%20&%20Linux-blue?style=flat)
[![On GitHub](https://img.shields.io/badge/on%20GitHub-True-green?style=flat&logo=github)](https://github.com/CastellaniDavide/osstats)

## Tags
 #tpi, #os, #python3, #filesys, #attributes, #cross-platform

## Description
View the proprieties of every file in a selected folder or in the subfolders.

## Required
 - python3 (I used Python 3.7 64 bit)
   - bs4 library (by the v 01.03) 
 - a web connection (by the v 01.03)

---
### Directories structure
 - bin
	 - osstat.py
 - doc
	 - README.md
 - flussi
     - osstat_w.csv
     - osstat_x.csv
 - log
	 - log.log

---
### OS supprted
 - Windows
 - Linux

---
### Execution examples
 - Default
   - osstat.py 
 - Personalized folder
   - osstat.py .. 

---
## Changelog
- [02.01_2020-5-14](#02.01_2020-5-14)
- [01.03_2020-5-5](#01.03_2020-5-5)
- [01.02_2020-4-28](#01.02_2020-4-28)
- [01.01_2020-4-28](#01.01_2020-4-28)

---
### 02.01_2020-5-14
 - correct some bugs
 - log output updated
 - now gives you more infos abot file proprieties
 - now there the output file is divided in two files
   - |   OS  |  file name |
     |  ---  |     ---    |
     |Windows|osstat_w.csv|
     | Linux |osstat_x.csv|

---
### 01.03_2020-5-5
 - now the data in friendly mode is converted by a WebService
 - now cros-sys platform
 - added a debug flag (default False) to manage better the program

---
### 01.02_2020-4-28
 - now the infos of every file are printed int the csv file in the folder flussi

---
### 01.01_2020-4-28
 - first version

---
Made by Castellani Davide
If you have any problem please contact me:
- davidecastellani@castellanidavide.it