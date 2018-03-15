

def executemhc(version, list_of_files):
	
	import datetime
	print datetime.datetime.now()
	import glob, os
	import threading
	
	path = raw_input("\nPlease enter the path to netMHC folder, ex: /home/prathyusha/NetMHC_4.0_for_Linux/netMHC-4.0: ")
	
	num = raw_input("\nPlease enter which length peptides you want to predict; if multiple lengths, seperate numbers with space 8 9 10 11: ")
	input_list = num.split()
	input_list = [int(a) for a in input_list]


	allele=raw_input("\nPlease enter the allele you want to predict; ex- H-2-Kb or HLA-A0301: ")

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
