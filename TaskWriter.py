'''
									 _______  _______  _______  _______    ______   _______          
									/ ___   )(  ____ \(  ____ )(  ___  )  (  __  \ (  ___  )|\     /|
									\/   )  || (    \/| (    )|| (   ) |  | (  \  )| (   ) |( \   / )
									    /   )| (__    | (____)|| |   | |  | |   ) || (___) | \ (_) / 
									   /   / |  __)   |     __)| |   | |  | |   | ||  ___  |  \   /  
									  /   /  | (      | (\ (   | |   | |  | |   ) || (   ) |   ) (   
									 /   (_/\| (____/\| ) \ \__| (___) |  | (__/  )| )   ( |   | |   
									(_______/(_______/|/   \__/(_______)  (______/ |/     \|   \_/   
                                                                 


************************************************************************
This is a simple python application for writing your dail program 
Creator : ZeroDay Email Address : Whoiskoorosh@gmail.com
This Program will get update sometimes.
*********************************************************
'''
#Start
#Import Module that neeededs
import os,time
from datetime import datetime
import sys
import csv


#Define the function for Clearing the page, For Writing the sentences Word by word  in one line  

def clear():
	os.system('clear')

def print_word_by_word(senstense):
	sen_len = len(senstense)
	for i in range(sen_len):
		print(senstense[i],end='',flush=True);time.sleep(0.1)
#######################################################################################3

clear()

print("Hello Friend")
time.sleep(1)

print("""

 _______  _______  _______  _______    ______   _______          
/ ___   )(  ____ \(  ____ )(  ___  )  (  __  \ (  ___  )|\     /|
\/   )  || (    \/| (    )|| (   ) |  | (  \  )| (   ) |( \   / )
    /   )| (__    | (____)|| |   | |  | |   ) || (___) | \ (_) / 
   /   / |  __)   |     __)| |   | |  | |   | ||  ___  |  \   /  
  /   /  | (      | (\ (   | |   | |  | |   ) || (   ) |   ) (   
 /   (_/\| (____/\| ) \ \__| (___) |  | (__/  )| )   ( |   | |   
(_______/(_______/|/   \__/(_______)  (______/ |/     \|   \_/   ,Product


""")

time.sleep(3)

clear()

#Entering the main loop 

while True:

	end_or_no = False 
	exit_check = False
	life_cycle = False
# Menu 

	print("""ZeroDay, Task Writer.
	\nFor:
	1-Today
	2-Custom
	3-info
		""")

#Get the Menu Input

	while  True:
		while True:
			try:
				date = int(input("Select your option => "))
				break
			except:
				print("Please Enter 1 Or 2 nothing Else Friend.")
				time.sleep(1)

		if(date == 1):
			date= datetime.today().strftime('%Y-%m-%d')
			life_cycle = True #For Continuing to the last session 
			break

		elif(date == 2):
			print("\n")
			date = input("Enter the date you want: ")
			life_cycle = True #For Continuing to the last session 
			break

		elif(date == 3):#INFO Session
			
			clear()
			welcomer = "Thanks for using my program 'ZeroDay Task Writer' "

			print_word_by_word(welcomer)

			word = """\nIn fact this is a simple python application that you can write your Tasks with it and keep them for your self in a text file.
			The Creator is : Zero Day 
			Email Address : whoiskoorosh@gmail.com"""

			print_word_by_word(word)
			exit_check = True # FOR ASKING DO YOU WANT TO EXIT OR NOT 
		
		

		else:
			date= datetime.today().strftime('%Y-%m-%d')
			print("Well, It seems like u want to broke the Program so we set the Default Value for you.")
			time.sleep(6)
			status1 = False
	
		if(exit_check == True): #EXIT CHECK
			while True:
				try:
					check_for_continue = input("\nDo you want to continue Y/N?!")
					if (check_for_continue.lower() == 'y'):	
						clear()
						end_or_no = True
						break
					elif(check_for_continue.lower() == 'n'):
						clear()
						print('GoodBye Friend !')
						time.sleep(1)
						break
						
					else:
						print(" Yes(Y) or No (N) ?")
						time.sleep(2)
						clear()
				except:
					print("Well the program continued")
					time.sleep(0.5)

		break
	if(life_cycle == True): #Life Cycle Last Mission

		clear()
		mission = 'well GOOD LUCK Friend'

		print_word_by_word(mission)

		clear()


		jobs_dic = [date]

		job = input("Enter the task: ")
		jobs_dic.append(job)


		print("****************** write exit for quiting the software ******************")
		time.sleep(3)

		clear()

		counter = 1

		while True:
		
			counter += 1		
			job = input("Enter the task %s : "%counter)
			if(job.lower() == 'exit'):
				file_name = input("Enter the file name  => ")
				file_name = file_name + ".txt"
				file = open(file_name,'w+')
				for i in jobs_dic:
					file.write("%s \n"%i)
				file.close()
				
			else:
				jobs_dic.append(job)

		#Say goodbye to the friend 
			
			print("We wroted your schedule for tommorow Goodbye Friend :)")
			time.sleep(3)
			end_or_no = False
			break

	if (end_or_no == True):
		pass
	else:
		break

