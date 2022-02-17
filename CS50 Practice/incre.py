
# python do not support increment ++ & decrement --

counter  = 0

# method 1
counter = counter + 1
print("Counter: ", counter)
# In python we  use + sign for concatinating Strings i.e pint("Counter: " + counter) = error
# Hence we use , (comma) to concatinate int to str 

# To avoid such confussion better way is to use "print format"
# method 2
counter += 1
print(f"Counter: {counter}")
