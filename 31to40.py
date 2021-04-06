#Question 31
#FromScratch - Create a script that generates a file where all letters of English alphabet are listed one in each line
#TO BE USED AS FIRST LECTURE EXAMPLE
#SOLUTION WOULD BE LIKE: Think of the program as a machine that gets some input and produces some output.
#In this case the input would be alphabet letters and the output a file with the alphabet letters. And between we need to use every tool that we can to make that happen.

#Question 32: Print out in each line the sum of homologous items from the two sequences
a = [1, 2, 3]
b = (4, 5, 6)

#Question 33: Create a script that generates a file where all letters of English alphabet are listed two in each line

#Question 34: #Write a script that extracts letters from files if letters are contained in "python" and puts the letters in a list

#Question 35: The code is supposed to ask the user to enter their name and surname, and then it prints out those user submitted values. 
#Instead, the code throws a TypeError. Please fix it so that the expected output is printed out.
firstname = input("Enter first name: ")
secondname = input("Enter second name: ")
print("Your first name is %s and your second name is %s" % firstname, secondname)

#Question 36: #Print out the last name of the second employee
d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}

#Question 37: Change the last name of the second employee and store the dict d1 to a json file
from pprint import pprint
d1 = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}


#Question 38:Print out three lines saying for instance item 1 has index 0, and so on.
a1 = [1, 2, 3]

#Question 39: Create a program that prints Hello repeatedly.


#Question 40: Create a program that prints Hello repeteadly after 1 second first, then after 2, 3, 4 increasing the interval by one




#Answears

#Q31:
#import string
#with open("letters.txt", "w") as file:
#    for letter in string.ascii_lowercase:
#        file.write(letter + "\n")

#Q31:
#for i, j in zip(a, b):
#    print(i + j)

#Q32:
#import string
#with open("letters.txt", "w") as file:
#    for letter1, letter2 in zip(string.ascii_lowercase[0::2], string.ascii_letters[1::2]):
#        file.write(letter1 + letter2 + "\n")

#Q33:
#import glob
#letters = []
#file_list = glob.iglob("letters/*.txt")
#check = "python"
#for filename in file_list:
#    with open(filename,"r") as file:
#        letter = file.read().strip("\n")
#        if letter in check:
#            letters.append(letter)
#print(letters)


#Q34:
#firstname = input("Enter first name: ")
#secondname = input("Enter second name: ")
#print("Your first name is %s and your second name is %s" % (firstname, secondname))

#Q35: #print(d['employees'][1]['lastName'])

#Q36:

#Q37:
#import json
#d1['employees'][1]['lastName'] = "Smooth"
#pprint(d)
#with open("company1.json", "w") as file:
#    json.dump(d, file, indent=4, sort_keys=True)

#Q38:
#for index, item in enumerate(a):
#    print("Item %s has index %s" % (item, index))

#Q39: 
#while 1 < 2:
#    print("Hello")

#Q40:
#import time
#i = 0
#while True:
#    print("Hello")
#    i = i + 1
#    time.sleep(i)



