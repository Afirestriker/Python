
#Add each line of a file to a list, and display that list.

list1 = []

f1 = open("file1.txt")
for x in f1:
    list1.append(x)

print(list1)
