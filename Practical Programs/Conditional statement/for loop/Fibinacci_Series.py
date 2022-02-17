
# Accept a number of terms from user, and print fibonacci series

n = int(input("Enter number of terms: "))

a=0
b=1
print(a, end="  ")
print(b, end="  ")
for x in range (2, n):
    c = a+b
    print(c, end="  ")
    a=b
    b=c
