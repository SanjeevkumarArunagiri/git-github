# Guessing the numerb
from random import randint

nameoftheperson = input("Hello, Please enter your name : ")
number = randint(0,10)
print(number)
numberofguess = 0
print(f"Hello {nameoftheperson}, Please select any number between 0 to 10")
while numberofguess < 3:
    numberofguess += 1
    guess = int(input("Please enter the number : "))
    if (number > guess):
        print("number is too less ")
    elif (guess > 10):
        print("Invalid entry, Please enter the proper number")
    elif( number < guess) and (number ):
        print("number is too large")
    elif (guess == number):
        print(f" you are right, the hidden number is {number}. YOU WIN !!")
        break