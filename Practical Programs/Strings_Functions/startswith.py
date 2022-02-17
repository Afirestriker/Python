
# startswith()
# --> return bool true, if the given string start with the same character that we pass to function startswith()

# Note: startswith() matches for exact match i.e. Hello and hello are different

str1 = "Hello python"
str2 = "Hello"

if(str1.startswith(str2)):
    print("Yes")
else:
    print("No")
