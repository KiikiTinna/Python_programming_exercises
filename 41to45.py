#Question 41: Create a function that takes a word from user and translates it using a dictionary of three words, 
#returning a message when the word is not in the dict,
# considering user may enter different letter cases
d = dict(weather = "clima", earth = "terra", rain = "chuva")



#Question 42: Print out the text of this file www.pythonhow.com/data/universe.txt. 
#Count how many a the text file has


#Question 43:Create a script that let the user type in a search term and opens and search on the browser for that term on Google 

#Question 44: Plot the data in the file provided through the URL http://www.pythonhow.com/data/sampledata.txt

#Question 45: Create a script that gets user's age and returns year of birth


#Answers

#Q41:
#def vocabulary(word):
#    try:
#        return d[word]
#    except KeyError:
#        return "That word does not exist."

#word = input("Enter word: ").lower()
#print(vocabulary(word))

#Q42:
#import requests
#response = requests.get("http://www.pythonhow.com/data/universe.txt")
#text = response.text
#print(text)
#count_a = text.count("a")
#print(count_a)

#Q43:
#import webbrowser
#query = input("Enter your Google query: ")
#url = "https://www.google.com/?gws_rd=cr,ssl&ei=NCZFWIOJN8yMsgHCyLV4&fg=1#q=%s" % str(query)
#webbrowser.open_new(url)

#Q44:
#import pandas
#import pylab as plt
#data = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
#data.plot(x='x', y='y', kind='scatter')
#plt.show()

#Q45: 
#from datetime import datetime
#age = int(input("What's your age? "))
#year_birth = datetime.now().year - age
#print("You were born back in %s" % year_birth)
