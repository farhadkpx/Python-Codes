
#dict is muttable

dict = {'Name':'Manju', 'Age':'25','Sub':'CS'}
print dict

print dict['Name']
dict['Age']=23
print dict

print dict.keys()
print dict.values()


#traverse the dictionary

for key in dict.keys():
	print dict[key]
	
#dict.update{['clg':'sapthagiri','gender':'Male']} #used to update the key/value in dictonary

print dict
#delete the element from the dictionary

del dict['Age']   # wont give the val but deletes
print dict

val = dict.pop('Sub') #If you want to store the deleted value use pop
print val
print dict

dict1 = {}
str = ' This is is a python learn learn program'
words = str.split()
for keys in words:
	if keys not in dict1:
		dict1[keys] = 1
	else:
		dict1[keys] = dict1[keys] + 1

print dict1
		
		
	
