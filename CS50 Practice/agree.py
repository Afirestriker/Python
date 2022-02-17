
# Reducing redundancy using if-ese in more smart way to check multiple condition in one line

ans = input("Do you agree? ").lower()

if ans in ["y", "yes"]:
    print("Agreed.")
elif ans in ["n", "no"]:
    print("Not agreed.")
else:
    print("Nor agreed, nor disagreed.")
