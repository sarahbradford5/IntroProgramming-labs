#CMPT 120 Intro to Programming
# Lab #6 - Control and Program Design 
# Author: Sarah Bradford


# gloabal list
colors = ["blue" , "green" , "purple" , "yellow" , "red"]

def showTitle():
    print("Color Preferance Evaluator")

def promptForColor():
    color = input("please enter a color")
    color = color.strip()
    color = color.lower()
    return color 

def praiseUser():
    print("good choice!")

def ridiculeUser():
    print("bad choice, I dont like that color.")

def confirmColor():
    x=0
    color = promptForColor()
    while x == 0:
        check = "you entered {} Is it correct? (Y/N)\n".format(color)
        confirm = input(check)
        confirm = confirm.lower()
        if confirm[0] == "y":
            x=1
        elif confirm[0] == "n":
            x=0
        else:
            x=0
    return color 

def containsElement():
    x = 2
    color = confirmColor()
    while x==2:
        if color == colors[0] or color == colors[1] or color == colors[2] or color == colors[3] or color == colors[4]:
            x=1
            praiseUser()
        else:
            x=1
            ridiculeUser()


def main():
    showTitle()
    containsElement()

main()
        
        
