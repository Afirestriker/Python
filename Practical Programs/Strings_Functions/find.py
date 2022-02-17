
# The find() method finds the first occurrence of the specified value.
# The find() method returns -1 if the value is not found.
# The find() method is almost the same as the index() method, the only difference is that the index() method raises an exception if the value is not found.

str1 = "Asia India"
str2 = "Asia"

str3 = str1.find(str2)

if(str3 > -1):
    print("Found")
else:
    print("Not found")
