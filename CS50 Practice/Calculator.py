
# Accept two int value from user, and perform addition

#input() returns String value, and so we type case String to int using int()
x = int(input("Enter X: "))
y = int(input("Enter Y: "))

print(x+y)

# Truncation 
# in C dividing int/int we have to truncate each value in float to get float value i.e (float)int/(float)int
# But in python that's not the case

# Note: here we do not truncate (float)x / (float)y, like we has to do in C
z = x/y
print(z)

# though to get C like output we can use double //
zz = x//y
print(zz)
