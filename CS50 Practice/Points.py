
# Program to determine how many points is lose, Fewer or More or Same

points = int(input("How many point did you lose? "))

if(points < 2):
    print("You lost fewer points than me.")
elif(points > 2):
    print("You lose more points than me.")
else:
    print("You lose same number of points as me.")
