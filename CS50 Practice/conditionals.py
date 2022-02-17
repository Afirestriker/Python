
# Conditionals statement writting in python

# INDENTATION IN PYTHON IN IMPORTANT

# In python instead of curly braces {}, indentation is used for specifying specific blocks of code
# Hence indentation i.e Styling your program propery is very important when writting code in python

x = 2 
y=4

# if statment
if x<y:  #in python parenthesis () is optional for condition, but might need when using logical operators
    print(f"{x} is smaller than {y}")

# if-else statement
if x>y:
    print(f"{x} is greater than {y}")
else:
    print(f"{x} is smaller than {y}")

# if elif else statment
if x>y:
    print(f"{x} is greater than {y}")
elif x<y:
    print(f"{x} is smaller than {y}")
else:
    print("Both are equal")

