
# Open a file and write to that file
# Note: if file is open in write mode 'W', and perform f.write() the whole file will be overwritten

fop = open("file1.txt", "w")
fop.write("Overriding the complete file")
fop.close()

f = open("file1.txt")
for x in f:
    print(x)