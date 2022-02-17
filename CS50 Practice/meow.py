
# demonstration of how we could write the code more readable using main()

# main() includes the main part of code
def main():
    meow(3)

# here we define the rest of function
def meow(n):
    for i in range(n):
        print("Meow")

# Note: main() function is called at the very last, since python is an interpreter language,
#  and it is necessary to have all the function / keyword to be define before they are used.
#  and calling main() at the last mean that python have interpreted all the code that will be needed.
#  plus point: the code is more readable, as the main part of code is inside main().
main()
