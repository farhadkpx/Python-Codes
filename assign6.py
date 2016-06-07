''' Function to compute the max of 3 nos'''
def max_of_three(a,b,c):
	max = a
	if (a > b and a > c):
		max = a
	elif(b > max and b > c):
		max = b
	elif(c > max and c > b):
		max = c
	else: 
		pass
	return max
	
'''Function to compute the string length'''
def complen(s):
	s = s+'\n'                           #append the '\n' for the comparison later
	list = []							 #Empty list and assign the string with the delimiter
	list = s
	i = 0
	count = 0
	while(True):
		if (list[i] != '\n'):			# Compare character by character to find out the length
			count = count+1
			i = i+1
		else:
			break
	return count

''' Function to find the reverse of a no'''	
def reverse(sen):
	j = complen(sen)					#compute length of the string from the complen function defined above
	list1 = []
	list1 = sen
	while(True):
		if(j == 0):
			break;
		else:
			print list1[j-1],			#print the character by character 
			j = j-1
	print "\n"
	
'''Function to take the input for finding out the largest of 3 nos'''	
def large():			
	try:	
		arg1 = int(raw_input("Enter the first no? : "))
		arg2 = int(raw_input("Enter the second no? : "))
		arg3 = int(raw_input("Enter the third no? : "))
		print "Maximum of three nos", max_of_three(arg1,arg2,arg3)   #call the max_of_three function to compute the largest of three nos
	except:
		print "Enter the appropriate values"
		
		

	
'''Function to take the input to find the length of the string'''
def lenofstr():
	try:
		str = raw_input("Enter the string? : ")
		print "The length of the string is ",complen(str)
	except:
		print "not right"
		
			

''' Function to take input for the string reversal'''
def reverseofstr():
	rev = [] 
	rev = raw_input("Enter the Str you want to reverse ?: ")
	print "original string \n",rev
	print "String reverse is "
	reverse(rev)
	

''' Menu to decide which program to exceute'''
			
def menu():
	try:
		while (True):
			print lis
			choice = int(raw_input("Enter the choice from the above, 99 or any other to abort ?: "))
			if(choice == 1):
				large()
				break
			elif(choice == 2):
				lenofstr()
				break
			elif(choice == 3):
				reverseofstr()
				break
			elif(choice == 99):
				exit(0)
			else:
				pass
	except:
		print "Going to quit"
		exit(0)
		
		
			
		

lis = ['1:Largest of 3 nos','2:Length of String','3:String Reverse']
menu()

