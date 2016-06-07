
#file handler for write mode

#fhand = open(wrt.txt)

while True:
	mth = raw_input("Enter the mode in which you want to open:")
	if mth !='w' and mth!='a':
		print "Enter the proper method"
	else:
		break
	
	
fhand = open('wrt.txt',mth)  #write mode




print "Type the file name you want to open or END at the last"
while True:
	line = raw_input("> ")
	if line == 'END':
		exit()
	fhand.write(line)
	fhand.write("\n")

fhand.close()
	
