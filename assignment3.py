import os.path
#file handler for write mode
path = "C:\Users\Manju-PC\trainings"

while True:
	file_name = raw_input("Enter the filename you want to create or write to?: ")
	mth = raw_input("Enter the file method w/a for write/append : ")
	if (os.path.exists(file_name)==False) and mth == 'a':
		print "Enter the existing filename from the working dir c:\users\manju-pc\trainings"
	elif mth != 'a' and mth != 'w':
		print "Kindly enter the correct method and try again"
	else:
		break

fhand = open(file_name,mth)   #write 

print "Type your lines or 'END' for end it"
while True:
	line = raw_input("==> ")
	if line=='END':
		exit()
	fhand.write(line)
	fhand.write("\n")
	
fhand.close()