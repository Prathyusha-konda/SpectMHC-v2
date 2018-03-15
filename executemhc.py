import csv, sys, math

path = sys.argv[1]
ver = sys.argv[2]
ifile = sys.argv[3]
mhc = sys.argv[4]
len = sys.argv[5]

executemhc(ver, ifile)


def executemhc(version, list_of_files):
	
	import datetime
	print datetime.datetime.now()
	import glob, os
	import threading
	
	path = path
	
	#num = raw_input("\nPlease enter which length peptides you want to predict; if multiple lengths, seperate numbers with space 8 9 10 11: ")
	#input_list = num.split()
	#input_list = [int(a) for a in input_list]
	input_list=len

	allele=mhc

	out_list = []
	for i in input_list:	
		for filename in list_of_files: 

			head, sep, tail = filename.partition('.f')
			print '\nfile %s is executed' %head 
			
			outfile='%s_%d_output.txt' %(head, i)
			out_list.append(outfile)
			
			if version in '4.0':
				command = '%s/netMHC -l %d -a %s %s > %s' %(path, i, allele, filename, outfile)
			elif version in 'pan':
				command = '%s/netMHCpan -l %d -a %s %s > %s_%d_output.txt' %(path, i, allele, filename, outfile)			
			elif version in '3.4':
				command = '%s/netMHC -l %d -a %s %s > %s' %(path, i, allele, filename, outfile)
			os.system(command)

	print "\nnetMHC execution completed"
	
	return out_list
