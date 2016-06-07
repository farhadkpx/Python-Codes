import mylib

def amk(a,b,c,*args,**kwargs):
	print a,b,c
	print args		#args takes only the extra arguments apart from default values
	print kwargs   #kwargs takes the parameters with the default values alone
	
	
amk(4,5,6,7,84,p=3,q=2)

