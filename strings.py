
str = 'We are learning python'

for i in range(len(str)):
	pass
	#print (str[i],)
	

for char in str:
	print (char)
	
# any string is always a list

# strings are immutable in python

for word in str.split():
	print (word)

#str='We|are|learning|python"

str ='-------------------this----------------------'
print (str)
print (str.lstrip('-'))
print (str.rstrip('-'))
print (str.strip('-'))
