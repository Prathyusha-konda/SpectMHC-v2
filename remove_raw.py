import csv, sys, math

ifile = sys.argv[1]

del_temp_files(ifile)

def del_temp_files(list_of_temp_files):
	import os
	for filename in list_of_temp_files:
		os.remove(filename)
	print "\nThe raw netmhc files are removed."
