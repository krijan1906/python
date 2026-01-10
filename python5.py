import random
num1=random.randint(1, 10)
print("lets play the number gusessing game you can choose a number 1-10")
guess=int(input("enter your guess "))
if num1==guess:
    print("congratulation you guessed the correct number")

else:
    print("sorry you guessed the wrong number the correct number was", num1)