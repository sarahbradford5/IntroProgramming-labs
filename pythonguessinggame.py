def main():
    print("GUESSING GAME")
    x=2

    while x==2:
        b=input("im thinking of an animal, can you guess what it is?")
        s="dog"

        if s==b:
            x=1
            print("congratulations, you are correct!")
            
        else:
            print("sorry, thats not correct, try again")


main()
