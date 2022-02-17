
# Python Exceptions
# Exception are generally a error which will not be detected until you run your code, 
# Exception are so called as Run-time Error

try:
    x = int(input("Enter X: "))
except:
    print("That is not an int!")
try:
    y = int(input("Enter Y: "))
# Looking for more specific error
except ValueError:
    print("That is not an int!")
    
print(x+y)

flo = float(2.8)
print(flo)

