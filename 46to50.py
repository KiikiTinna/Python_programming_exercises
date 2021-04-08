#Question 46: Create a program that generates a password of 6 random 
#alphanumeric characters in the range abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?

#Question 47: Create a script that lets the user submit a password until they have satisfied three conditions:
#1. Password contains at least one number
#2. Contains one uppercase letter
#3. It is at least 5 chars long
#Give the exact reason why the user has not created a correct password


#Question 48: Create a script that checks a list against countries_clean.txt
#and creates a list with items that were in that file
checklist = ["Portugal", "Germany", "Munster", "Spain"]

#Question 49: Create a script that uses countries_by_area.txt file 
#as data sourcea and prints out the top 5 most densely populated countries

#Question 50: Create a program that asks the user to submit text repeatedly
#The program closes when the user submits CLOSE


#Answers:

#Q46:
#import random
#characters = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
#chosen = random.sample(characters, 6)
#password = "".join(chosen)
#print(password)

#Q47:
#while True:
#    notes = []
#    psw = input("Enter password: ")
#    if not any(i.isdigit() for i in psw):
#        notes.append("You need at least one number")
#    if not any(i.isupper() for i in psw):
#        notes.append("You need at least one uppercase letter")
#    if len(psw) < 5:
#        notes.append("You need at least 5 characters")
#    if len(notes) == 0:
#        print("Password is fine")
#    else:
#       print("Please check the following: ")
#        for note in notes:
#            print(note)

#Q48:
#with open("countries_clean.txt", "r") as file:
#    content = file.readlines()
#content = [i.rstrip('\n') for i in content]
#checked = [i for i in content if i in checklist]
#print(checked)


#Q49:
#import pandas
#data = pandas.read_csv("countries_by_area.txt")
#data["density"] = data["population_2013"] / data["area_sqkm"]
#data = data.sort_values(by="density", ascending=False)
#for index, row in data[:5].iterrows():
#    print(row["country"])


#Q50:
#file = open("user_data.txt", 'a+')
#while True:
#    line = input("Write a value: ")
#    if line == "CLOSE":
#        file.close()
#        break
#    else:
#        file.write(line + "\n")
