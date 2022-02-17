
# Accept how many line from beginning of a file should be display
# Note: first line of the file is index as 0.

n = int(input("Enter number: "))
f1 = open("file1.txt")

count=0
for x in f1:
    # True for count=(0, 1, 2, 3) if n=4 = total 4 lines
    if(count < n):
        print(x)
        count+=1
