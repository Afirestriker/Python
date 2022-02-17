
# Print last n lines from a file

n = int(input("Enter Number: "))

list1=[]
f1 = open("file1.txt")
for x in f1:
    list1.append(x)

count=1
for y in reversed(list1):
    if(count<=n):
        print(y)
        count+=1

