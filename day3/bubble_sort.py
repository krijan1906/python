terms=int(input("enter the number of terms in tupples"))
tupples=[]
i=0
while i < terms:
    tupples[i]=int(input("enter the element:"))
    i=i+1
print("your unsortedd valur are:",tupples)    

for i in range(terms):
    for j in range(terms):
        if tupples[j]>tupples[j+1]:
            temp=tupples[j]
            tupples[j]=tupples[j+1]
            tupples[j+1]=temp

print("the sorted value is :",tupples)            

