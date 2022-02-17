
# Accept a, b and c. And print the quadratic expression

import cmath

a = int(input("Enter A: "))
b = int(input("Enter B: "))
c = int(input("Enter C: "))

x = b*b-4*a*c

r1 = cmath.sqrt(x)/2*a
r2 = cmath.sqrt(x)/2*a

print(f"R1: {r1}  & R2: -{r2}")

result = a*cmath.sqrt(x) + b*x + c
print("Result: ", result)
