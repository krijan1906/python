#tupple ,dictionary in python
personal_details=[
    {

        "name":"krijan",
        "age":15,   
        "gender":"male",
        "email":"krijanmaharjan31@GMAIL.COM",
        "phone":9876543210

    },
    {

        "name":"ashish",
        "age":30,   
        "gender":"male",
        "email":"ashish@GMAIL.COM",
        "phone":981234567

    },
    {

        "name":"ompandey",
        "age":28,   
        "gender":"male",
        "email":"ashihs31@GMAIL.COM",
        "phone":9876543210
    },
]
print("whose detail do you want to see krijan/ashish/ompandey")
name=input("enter the name:")
if name=="krijan":{
    print(personal_details[0])
}
elif name=="ashish":{
    print(personal_details[1])
}
elif name=="ompandey":{
    print(personal_details[2])
}
else:{
    print("no detail found")
}