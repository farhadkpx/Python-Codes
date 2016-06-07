#looping
#while and for looping

var=5
fruits=['Apple','Mango','Banana','Peach','Papaya','guava','water']

#while will execute till the command is TRUE
#indefinte loop

while var>0: 						#checking if var >0
	print (var)						 #printing var
	var = var-1						 # decrementing the var


#for looping
#finite looping
# for loop is executing for each values

for fruit in fruits:
	print(fruit,)
	
values = range(5)
sum = 0
for val in values:
	sum = sum + val
print (sum)

sum = 0
for val in range(5):
	sum = sum + val
print (sum)