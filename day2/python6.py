import random
num1=random.randint(1, 3)
if num1==1:
    choice1="rock"
elif num1==2:
    choice1="paper"
else:
    choice1="scissors"
print("let's play rock paper scissors")
user_choice=input("enter your choice (rock/paper/scissors): ").lower()
print("you chose:", user_choice)
print("computer chose:", choice1)
if user_choice==choice1:    
    print("it's a tie!")
elif user_choice=="rock" and choice1=="scissors":
    print("you win! rock crushes scissors.")
elif user_choice=="paper" and choice1=="rock":
    print("you win! paper covers rock.")
elif user_choice=="scissors" and choice1=="paper":
    print("you win! scissors cut paper.")
else:
    print("yout losee computer wins")