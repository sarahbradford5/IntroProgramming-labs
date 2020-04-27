#CMPT 120 Intro to Programming
# Lab #5 - Working with Strings and Functions
# Author: Sarah Bradford
# Created: 2020-02-24
def user():
     first = input("Enter your first name: ")
     last = input("Enter your last name: ")
     return first,last

def email():
     first, last = user()
     uname = str(first+"."+last)
     return uname


def length():
     y = 0
     pswd = input("Create a password: ")
     notCorrectLen = False
     if len(pswd)<8:
         notCorrectLen = True
     while notCorrectLen:
          print("password not long enough, must be 8 characters")
          pswd = input("Create a new password: ")
          if len(pswd)<8:
             notCorrectLen = True
          else:
               notCorrectLen = False
          while y==0:
               if (pswd.islower()) == False and (pswd.isupper()) == False:
                    print ("strong password")
                    y=1
               if (pswd.isupper())== True or (pswd.islower()) == True:
                    y=0
                    print("password must contain upper and lowercase letters")
                    pswd=str(input("please enter a new password "))

     return pswd
               
                       
def main():
     uname=email()
     pswd = length()
     print("ok! Your new email address is", uname.lower(),"1@marist.edu")
     

main()
