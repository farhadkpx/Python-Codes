
#open a file handle
file_name = "test.txt"

#creating a file handler
fhand = open("test.txt")

#print fhand
count=0
#reading the files and the list of lines
for line in fhand:
	line = line.rstrip()  #remove the extra spaces and new line
	print line
	count = count+1

print "Total lines are",count

fhand.seek(0,0)
#read - this will read the whole file in one go

print "\n This is an example for file reading"
print fhand.read()


fhand.seek(0,0)
#readline - this will read one line at a time
print "\n This is a readline method"
print fhand.readline()
print fhand.readline()


