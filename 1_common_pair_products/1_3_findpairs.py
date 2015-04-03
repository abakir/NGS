#!/usr/bin/python

from __future__ import with_statement
import csv, re

@outputSchema("Name:chararray")

def find(item, path):

	with open(path, 'r') as file:
		rowdata = []
		reader = csv.reader(file)
		for row in reader:
			rowdata.append(row)

		for i in range(0, len(rowdata)-1):
			if re.match(item, rowdata[i][0]):
				lis = []
				print "found" + str(i)
				for j in range(i+1, len(rowdata)-1):
					flag = 0
					for k in range(1, len(rowdata[i])-1):
						for l in range(1, len(rowdata[j])-1):
							if ((rowdata[i][k]) is not None) and ((rowdata[j][l]) is not None):
					
								if re.match(rowdata[i][k], rowdata[j][l]):
									flag = flag + 1					
					if flag > 0:
						#print flag
						lis.append(rowdata[j][0])
						lis.append(flag)
				return lis	


