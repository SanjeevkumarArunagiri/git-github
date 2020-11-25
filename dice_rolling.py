from random import randint
min = 1
max = 6
# roll_again = "Yes"
usr_input = input("if u want to roll dice, Pls enter yes : ")
while usr_input.lower() == "yes" or usr_input == "y" or usr_input.lower() =="no" or usr_input == "n":
    if usr_input =="yes" or usr_input == "y":
        print("rolling the dice")
        print("and the value is ....")
        num1 = randint(min,max)
        num2 = randint(min,max)
        print(num1,num2)
    elif usr_input =="no" or usr_input == "n":
        print("Done here !!")
        break
    print("Do you want to roll the dice again ??")
    usr_input = input("yes or no : ")

    print("its jst for test only...")