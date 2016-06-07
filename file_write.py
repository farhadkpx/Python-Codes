
#file handler for write mode
'''
fhand = open(test.txt)   # default is read
fhand = open(test.txt,'r')   # default is read
'''
while True:
	mth = raw_input("Enter the file method w/a for write/append : ")
	if mth != 'a' and mth != 'w':
		print "Kindly enter the correct method and try again"
	else:
		break

fhand = open('filewrt.txt',mth)   #write 
#fhand = open(test.txt,'a')   #append

print "Type your lines or 'END' for end it"
while True:
	line = raw_input("==> ")
	if line=='END':
		exit()
	fhand.write(line)
	fhand.write("\n")
	
fhand.close()