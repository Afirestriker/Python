
# Take input from user as number and power, and print the number^power, using logic and not predefine function

n = int(input("Enter Number: "))
p = int(input("Enter Power: "))
m=1

# directly using exponent
print(n**p)

# using logic
for i in range(1, p+1):
    m = m*n
print(m)
