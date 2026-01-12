print("multiplication table")
number=int(input("enter the number of which you want to find the multiplication table: "))
for i in range(1,11):
    result=number*i
    print(number,"x",i,"=",result)
    