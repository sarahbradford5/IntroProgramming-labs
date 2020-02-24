import math
def pi():
    n=eval(input("enter the number of the terms you would like to be summed\n"))
    denominator=1
    numerator=4
    sum=0


    for i in range (n):
        sum = (numerator/denominator)+sum
        denominator = denominator + 2 
        numerator = -1 * numerator

    print(sum)
    print("this number is", math.pi-sum, "away from pi")

pi()

#citation: worked with Jadyn Kennedy
