
# Display total count of line in a file

f1 = open("file1.txt", "r")
count = 0

for x in f1:
    count +=1

print("Total number of lines: ", count)
