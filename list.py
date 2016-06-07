

#list
# mutable, multiple data type, un-ordered

lis = [1,2,3,4,5,6,7,8,9] #nos
lis2 = ['atul','manju','rochan'] #strings
lis3 = [1,'This',2,'me','there'] #both

#create empty list
lis4 = [] #empty
lis5 = list() #empty

#traversl

for item in lis:
	print (item),
	
#slicing

print (lis[:],lis[2:3],lis[3:])

#Mutable
lis[5] ='Singh'

print (lis)

print (lis2)

#addition using + operator only for single element
lis2 = lis2 + ['manju']
#to concatenate using append only single element
lis2.append('newval')
print (lis2)

#for more values addition to the list
lis2.extend(['one','two'])

print (lis2)

#addition of elements in a specified place in the list
lis2.insert(5,'fifth')
print (lis2)

#list inside an other list
#lis2.insert(0,['start','element'])
print (lis2)

#accessing list inside the list
print(lis2[0][0])  #prints 'start'
print(lis2[0][1])  #prints 'element'

#removing the elements from the list
#pop
lis2.pop()  #removes the last element always
print (lis2)
lis2.pop()
print (lis2)


rval1=lis2.pop()
rval2=lis2.pop()
print (lis2)
print (rval1,rval2)

print (len(lis2))   #0,13
# index or indicies deletion - del(not returned deleted elements)
del lis2[1]
print (lis2)
#range to delete
del lis2[1:3]
print (lis2)

#delete the element by values

lis2.append('three')
print(lis2)
lis2.remove('three')
print (lis2)

lis2.append('one')
lis2.append('two')
lis2.append('three')
#sort the list
lis2.sort()
print (lis2)
#lis.sort(reverse=True)
print (lis2)
Name = 'manjunath manikumar'
name_list = list(Name)
print (name_list)

#split
word_list = Name.split()
print (word_list)

#alias
print (lis3)
alias3 = lis3
print (alias3)

alias3[2] = 'changed'
print (lis3)
print (alias3)  #alias




