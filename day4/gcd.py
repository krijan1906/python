def gcd(a, b):
    while b != 0:
        temp = a
        a = b
        b = temp % b
    return a

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("GCD is:", gcd(num1, num2))