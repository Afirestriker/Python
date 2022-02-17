
# Check given number is prime or not

# method 3 - uing flag

n = int(input("Enter Number: "))
flag=0
i=2

while(i<=n//2):
    if(n%i==0):
        flag=1
        break
    i+=1

if(flag==0):
    print("Prime Number")
else:
    print("Not a prime number")
