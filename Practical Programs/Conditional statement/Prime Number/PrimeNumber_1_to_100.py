
# Print prime numbers from 1 to 100

for n in range(2, 100):
    f=2
    while f <= n//2:
        if(n%f == 0):
            break
        f+=1
    
    if f > n//2:
        print(n)
    