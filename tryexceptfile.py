#count the no of lines in a text file

file_name = raw_input("Enter the file name: ")

try:
	fhand = open(file_name)
except:
	print "File doesnt exist"
	fhand = open('test.txt')
	#exit()
	
count = 0
for line in fhand:
	line = line.rstrip()
	words = line.split()  #This will split the sentence into the sequence of words
	#count=count+1
	if 'python' in words:
		print "Yes you have a word python"
		print line
		count=count+1

print "Total no of lines with python are", count

fhand.seek(0,0)
#another method
for line in fhand:
	line = line.rstrip()
	if 'python' not in line:
		print line