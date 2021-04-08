#Question 51:Please download the database file database.db. 
#The file contains a table with 50 country names along with their area in square km and population.
#Please use Python to print out those countries that have an area of greater than 2,000,000.


#Question 52: Please download the database file database.db 
#use Python to access the database table rows that have an area of 2,000,000 or greater.
#Then export those rows to a CSV file


#Question 53: Create a program that asks the user to submit text through a GUI

#Question 54:Create a program that asks the user to submit text through a GUI using tkinter

#Question 55: Create a program that asks the user to submit text a web app


#Answers:
#Q51:
#import sqlite3
#conn = sqlite3.connect("database.db")
#cur = conn.cursor()
#cur.execute("SELECT country FROM countries WHERE area >= 2000000")
#rows = cur.fetchall()
#conn.close()
#print(rows)
#for i in rows:
#    print(i[0])


#Q52:
#import sqlite3
#import pandas
#conn = sqlite3.connect("database.db")
#cur = conn.cursor()
#cur.execute("SELECT * FROM countries WHERE area >= 2000000")
#rows = cur.fetchall()
#conn.close()
#print(rows)
#df = pandas.DataFrame.from_records(rows)
#df.columns =["Rank", "Country", "Area", "Population"]
#print(df)
#df.to_csv("countries_big_area.csv", index=False)


#Q53:
#file = open("user_data_save_close.txt", 'a+')
#while True:
#    line = input("Write a value: ")
#    if line == "SAVE":
#        file.close()
#        file = open("user_data_save_close.txt", 'a+')
#    elif line == "CLOSE":
#        file.close()
#        break
#    else:
#        file.write(line + "\n")


#Q54:
#from tkinter import *
#window = Tk()
#file = open("user_gui.txt", "a+")
#def add():
#    file.write(user_value.get() + "\n")
#    entry.delete(0, END)
#def save():
#    global file
#    file.close()
#    file = open("user_gui.txt", "a+")

#def close():
#    file.close
#    window.destroy()

#user_value = StringVar()
#entry = Entry(window, textvariable=user_value)
#entry.grid(row=0, column=0)
#button_add = Button(window, text="Add line", command=add)
#button_add.grid(row=0, column=1)
#button_save = Button(window, text="Save changes", command=save)
#button_save.grid(row=0, column=2)
#button_close = Button(window, text="Save and Close", command=close)
#button_close.grid(row=0,column=3)
#window.mainloop()


#Q55:
#from flask import Flask, render_template_string, request
#app = Flask(__name__)
#html = """
#  		      <div class="form">
#              <form action="{{url_for('sent')}}" method="POST">
#  			        <input title="Your email address will be safe with us." placeholder="Enter a line" type="text" name="line" required> <br>
#                <button class="go-button" type="submit"> Submit </button>
#  		        </form>
#          </div>
#"""
#@app.route("/")
#def index():
#    return render_template_string(html)
#@app.route("/sent", methods=['GET', 'POST'])
#def sent():
#    line = None
#    if request.method == 'POST':
#        line = request.form['line']
#        with open("user_input_flask.txt", "a+") as file:
#            file.write(line + "\n")
#        return render_template_string(html)
#if __name__ == "__main__":
#    app.run(debug=True)
