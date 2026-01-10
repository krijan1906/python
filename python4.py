print("licence eligibility checking program")
age=int(input("enter your age "))
if age>18 and age<20:
    print("you are eligible for the bike and scutee licence")

elif age>=20 and age<=22:
    print("you are eligible for the car licence")
elif age>22:
    print("you are eligible for any licence")

else:
    print("you are not eligible for the licence")