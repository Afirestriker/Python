
#Accept sale price and cost price and display whether it is profit or lost

cp = int(input("Cost Price: "))
sp = int(input("Sale Price: "))

if(sp < cp):
    print("Lost of ", sp-cp)
elif(sp > cp):
    print("Profit of ", sp-cp)
else:
    print("No profit, No lost")
