
# Accept a number and check if its prime

# method 1

n = int(input("Enter Number: "))

i=2

while i<=n//2:
    if(n%i==0):
        print(f"{n} is not a prime number")
        break
    i+=1

if(i>n//2):
    print(f"{n} is a prime number")
