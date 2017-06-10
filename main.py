#!/usr/local/bin/python3
import csv
import sys

csvFile = sys.argv[1]
print ('Read data from ', csvFile)
stateReader = csv.reader(open(csvFile, newline=''), delimiter=',')
for row in stateReader:
	if(row[2] == 'High'):
		print(', '.join(row))
