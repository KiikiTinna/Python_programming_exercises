#Question 22: Make a script that prints out letters of English alphabet from a to z
#Hint: use python libraries 

#Question 23: Make a script that prints out numbers from 1 to 10

#Question 24: Write a function that calculates acceleration given the formula: a = (v2 - v1) / t2 - t1

#Question 25: #Write a function that calculates liquid formula taken from http://www.1728.org/spherprt.gif. When writing the function consider that r is always 10.

#Question 26: #What will the script output
c = 1
def foo():
    return c
c = 3
print(foo())


#Question 27: The script throws an error. Fix it so that the script prints the value assigned to c1 inside the function
def foo1():
    c1 = 1
    return c1
foo1()
print(c1)

#Question 28: Create a function that takes a string and returns the number of words


#Question 29: Create a function that takes a text file and returns the number of words


#Question 30: Create a function like in the previous exercise, but taking into consideration that commas without space can separate words.



#Answers:

#Q22: 
#import string
#for letter in string.ascii_lowercase:
   #print(letter)

#Q23: 
#for i in range(1,11):
    #print(i)

#Q24:     
#def acceleration(v1, v2, t1, t2):
#    a = float(v2 - v1) / float((t2 - t1))
#    return a
#print(acceleration(0,10,0,20))

#Q25:
#from math import pi
#def volume(h, r = 10):
#    v = ((4 * pi * r**3) / 3) - (pi * h**2 * (3*r - h) / 3)
#    return v
#print(volume(2))

#Q26:It will output the last value of c which is 3

#Q27: Add "global c" before "c=1". Worth mentioning that if you remove foo(), variable c will come as undifined because the function has not been run

#Q28: 
#def count_words(string):
#   string_list = string.split(" ")
#   return len(string_list)
#print(count_words("Hey there it's me!"))

#Q29: 
#def count_words(filepath):
#    with open(filepath, 'r') as file:
#        strng = file.read()
#        strng_list = strng.split(" ")
#        return len(strng_list)
#print(count_words("words1.txt"))

#Q30: 
#def count_words(filepath):
#    with open(filepath, 'r') as file:
#        string = file.read()
#        string = string.replace(",", " ")
#        string_list = string.split(" ")
#        return len(string_list)
#print(count_words("words2.txt"))


