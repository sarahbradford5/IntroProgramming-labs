#CMPT 120 Intro to Programming
# Lab #5 - Working with Strings and Functions
# Author: Sarah Bradford
# Created: 2020-02-24

def user():
     first = input("Enter your first name: ")
     last = input("Enter your last name: ")
     return first,last

def email():
     x=user()
     x = x[0] + "." + x[1]
     return x 

def password():
     x=email()
     pswd = input("Create a new password: ")
     notCorrectLen = False
     if len(pswd)<8:
         notCorrectLen = True
     while notCorrectLen:
          print("password not long enough")
          pswd = input("Create a new password: ")
          if len(pswd)<8:
             notCorrectLen = True
          else:
              notCorrectLen = False
     print("strong password")
     print("ok! Your new email address is", x +"1@marist.edu")
     
def main():
     password()
     

main()
