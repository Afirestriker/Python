
# Find factorial of given number using for loop

num = int(input("Enter number: "))
fact = 1

print("Factorial of ", num, ": ")
for x in range(2, (num+1)):
    fact = fact * x

print(fact)