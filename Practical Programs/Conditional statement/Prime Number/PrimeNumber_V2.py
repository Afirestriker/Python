
# Check if given number is prime or not 

# method 2

n = int(input("Enter number: "))

if(n==2 or n==3 or n==5 or n==7):
    print("Prime Number")
elif(n%2 != 0 and n%3 != 0 and n%5 != 0 and n%7 != 0):
    print("Prime Number")
else:
    print("Not a prime number")

