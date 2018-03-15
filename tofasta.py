import csv, sys, math

ver = sys.argv[1]
ifile = sys.argv[2]
coff = sys.argv[3]

process_data(ver, ifile, coff)

def process_data(version, filelist, cut_off):
	
	if version in '4.0':
		bad_words = ['high binders', 'iCore', '----', '#']
	
	elif version in 'pan':
		bad_words = ['#', 'training data', 'ICore', 'high binders', '------']

	elif version in '3.4':
		bad_words = ['binder threshold', 'Artificial Neural', 'affinity(nM)', '--------', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

	for filename in filelist:
		newname=filename.replace("output","data")
		print filename
		with open(filename) as oldfile, open(newname, 'w') as newfile:
			for line in oldfile:
				if not any(bad_word in line for bad_word in bad_words):
					if line.strip():
						newline=line.split()
						if version in '3.4':
							if float(newline[3])<cut_off:
								if cut_off<500:
									newfile.write(">>"+newline[5]+"_"+newline[3]+"_"+newline[6]+'\n'+newline[1]+'\n')
								else:
									newfile.write(">>"+newline[4]+"_"+newline[3]+"_"+newline[5]+'\n'+newline[1]+'\n')

						else:

							if float(newline[13])<cut_off:
								newfile.write(">>"+newline[10]+"_"+newline[13]+"_"+newline[1]+'\n'+newline[2]+'\n')

	

	print "\nnetMHC processing complete"
