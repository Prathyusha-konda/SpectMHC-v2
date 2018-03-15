

num = raw_input("\nPlease enter which length peptides you want to predict; if multiple lengths, seperate numbers with space 8 9 10 11: ")
input_list = num.split()
input_list = [int(a) for a in input_list]
return input_list
