
# Accept a string from the user and display only thoes lines, which content the given string.

str = input("Enter Word: ")

f1 = open("file1.txt")
for x in f1:
    if(x.find(str) > -1):
        print(x)
