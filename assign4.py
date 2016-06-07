filename = 'eg.txt'
list = [',','?','!','@','.',' ']				#list of special characters
try:
	fhand = open('eg.txt')
except:
	print "some issue with the file"
	exit(0)

str = fhand.read()								#read into a string for manipulation later
print " This is the content of the file \n", str

dict = {}

words = str.split()
for key in words:
	if key not in list:
			dict[key]=dict.get(key,0)+1
print "Word dictionary is as follows"
print dict

dict1 = {}
fhand.seek(0,0)                                 #place the pointer to the start of file
for slice in fhand:								#traversing the file pointer
	line = slice.strip()						#strip the new line
	#print line
	for keys in line.lower():					#converting to lower and check the key 
		if keys not in list:					# not in the list of special characters defined above
			dict1[keys]=dict1.get(keys,0)+1
print " Character dictionary is as follows"
print dict1	
fhand.close()
	


	
