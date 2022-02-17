
# Dispaly file content by swaping the case, i.e lower-case to upper-case & upper-case to lower-case

f1 = open("file1.txt")
for x in f1:
    print(x.swapcase())
