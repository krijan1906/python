alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
text=input("enter the text:").lower()
key=int(input("Enter the key: "))

    
for ch in text:
    if ch in alphabets:
        index=alphabets.index(ch)
        encryption_index=(index+key)
        print("the encrypted message id:",alphabets[encryption_index%26])


            



