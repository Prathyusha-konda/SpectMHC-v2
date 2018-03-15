

def split_files(split):
	def chunks(l, n):
    		n = max(1, n)
    		return [l[i:i + n] for i in range(0, len(l), n)]
	def new_string(x):
		temp = ">"
		for i in x:
			temp = temp+i+">"
		temp = temp[:-1]
		return temp
	filename = raw_input("\nEnter file name: ")
	number = int(raw_input("\nHow many number of sequences do you want per file? : "))
	split_list=[]


	def mkfile(x,i):
		f = open("split"+str(i)+"_"+filename,"w")
		splitfile='split%s_%s' %(str(i), filename)
		split_list.append(splitfile)
		f.write(x)
		f.close()
	
	

	f = open(filename, "r")
	splitted_file = f.read().split(">")

	new_files = chunks(splitted_file, number)

	count = 1
	for i in new_files:
		q = new_string(i)
		if count == 1:
			q = q[1:]
		mkfile(q,count)
		count=count+1

	return split_list
