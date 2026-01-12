import random

password="krijan"
enter_password=input("enter the password: ")
if enter_password==password:
    print("you are logged in wellcome krijan")

else:
    print("incorrect passwrod enter password again")

    print("did you forget your password? (yes/no)")
    forget_password=input("yes or no").lower()
    if forget_password=="yes":
       otp=random.randint(1000,9999)
       print("your one time password is:", otp)
       enter_otp=int(input("enter teh otp:"))
       if enter_otp==otp:
           new_password=input("enter your new password:")
           password=new_password
           print("your password has been changed successfully")

       else:
           print("you enter wrong otp")

    else:
        print("try logging in again later")