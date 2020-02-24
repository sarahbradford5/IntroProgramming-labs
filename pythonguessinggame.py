def main():
    print("GUESSING GAME")
    x=2

    while x==2:
        b=input("im thinking of an animal, can you guess what it is?\n")
        s="dog"
        b=b.lower() #allows user to input uppercase letters

        if s==b:
            x=1
            print("congratulations, you are correct!")
            h=input("do you like dogs? (yes/no)")
            if h[0]=="y":
                print("me too! i have a lab!")
            else:
                print("well thats unfortunate")
            
            
        else:
            j=input("sorry, thats not correct, try again?")

            if j[0]=="y":
                x = 2

            else:
                x=1
                print("okay, thanks for playing!")

main()

#citation: worked with Jadyn Kennedy 
