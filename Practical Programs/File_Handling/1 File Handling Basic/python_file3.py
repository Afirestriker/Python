
# Display the line from file whcih start with given string

f1 = open("file1.txt")

for x in f1:
    if x.startswith("This"):
        print(x)
