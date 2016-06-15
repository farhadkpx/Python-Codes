import random		#importing the random library 
#from random import randint		
lis = []

def rand(a,b):
	return random.randint(a,b)			#return the random variables 
	
def display():		
	try:
		play_flag = raw_input("Do you want to play ? (y/n): ")	#Choice for user to play or not
		return play_flag			#on 'n' the program will terminate
	except:
		return False				#Any other key will exit

def start_play():
	no = int(raw_input("Enter the range to end ? "))		#range can be from 0 - 20 depending on the user
	
	for n in range(4):						#take only 4 random nos into the list by calling the rand function
		lis.append(rand(0,no))
		
	print lis					#Jus for our understanding to print the list.. to be commented while actual execution
	user_chance = 0
	max_chance = int(raw_input("Enter the max chances yu want to give the user for the guess : "))			#defining the max chance for the user 
	flag = True
	while flag:
		if(user_chance < max_chance):
			inp = int(raw_input("Guess the no : "))			#user input to guess
			if inp in lis:
				print "You Won"
				#flag = False
				break
			else:
				user_chance = user_chance+1
				
				if user_chance >= max_chance:
					print "You Lost"
						#flag = False
					break
					
				print "Cmon you can do even better"
				
					
					
	
def call():
	if (display() == 'y'):			#check and display based on the input
		start_play()
		display()
	else:
		exit()
	
	
call()				#start of the actual program begins here




	



		

	
		
		
	
		
			
