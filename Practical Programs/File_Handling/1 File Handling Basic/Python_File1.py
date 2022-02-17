
# Open and Read a file

# By default, the file is open in read mode
file1 = open("file1.txt")

for x in file1:
    print(x)

file1.close()
# Note: You should always close your files, in some cases, due to buffering, 
# changes made to a file may not show until you close the file.
