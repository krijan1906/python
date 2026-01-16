import random
def password_cracker():
    computer_password=random.randint(1000,9999)
    
    for i in range(1,10):
        for j in range(1,10):
            for k in range(1,10):
                for l in range(1,10):
                    string1=str(i)+str(j)+str(k)+str(l)
                    
                    if int(string1)==computer_password:
                        print("password cracked:",string1)
                        return 0;
                 

password_cracker()