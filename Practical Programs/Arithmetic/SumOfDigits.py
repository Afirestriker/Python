
# Accept a number and display sum of its digits

n = int(input("Enter Number: "))

s=0
while n>0:
    d = n%10    # n%10 gives remainder i.e digit
    s = s+d
    n = n//10

# The double forward slash // in Python is known as the integer division operator. 
# Essentially, it will divide the left by the right, and only keep the whole number component.

print("Sum of digits: ", s)
