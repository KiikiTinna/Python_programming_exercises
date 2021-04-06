#Question 11:Create a script that generates a list of numbers from 1 to 20. Do not create a list manually.


#Question 12:Create a script that generates a list whose items are products of the original list items multiplied by 10


#Question 13:Create a script that converts all items of the range to strings
my_range = range(1, 21)


#Question 14: Complete the script so that it removes duplicate items from the list a. 
a = ["1", 1, "1", 2]


#Question 15: Create a dictionary of two keys, a and b and two values 1 and 2 for keys a and b respectively.


#Question 16: Print out the value of key b
d1 = {"a": 1, "b": 2}


#Question 17: Calculate the sum of value of key a and value of key b and print it out
d2 = {"a": 1, "b": 2}

#Question 18: Fix next lines so it prints out Smith
d3 = {"Name": "John", "Surname": "Smith"}
print(d3["Smith"])


#Question 19: Add a c key with a value of 3 to the dictionary and print out the updated dictinary
d4 = {"a": 1, "b": 2}


#Question 20: Find the sum of all values
d5 = {"a": 1, "b": 2, "c": 3}


#Question 21 :Filter out values of equal or greater than 2
#Note that for Python 2 you will have to use iteritems
d6 = {"a": 1, "b": 2, "c": 3}




#Answers:

#Q11: #my_range = range(1, 21) 
      #print(list(my_range))

#Q12: #my_range = range(1, 21)
      #print([10 * x for x in my_range])
  
#Q13: #print(map(str, my_range))
      #for i in map:
          #print(i)
    
#Q14: #a = list(set(a))
      #print(a)

#Q15: #d = {"a": 1, "b": 2}

#Q16: #print(d1["b"])

#Q17: #print(d2["b"] + d2["a"])

#Q18: #print(d["Surname"])

#Q19: #d4["c"] = 3
      #print(d4)

#Q20: #print(sum(d5.values()))

#Q21: #d6 = dict((key, value) for key, value in d6.items() if value <= 1)
      #print(d6)
      
