import random
z = "y"
while z == "y":
    x = random.randint(1,6)
    if x==1:
        print("Dice Rolled:")
        print("---------")
        print("|       |")
        print("|   0   |")
        print("|       |")
        print("---------")
    elif x==2:
        print("Dice Rolled:")
        print("---------")
        print("|       |")
        print("| 0   0 |")
        print("|       |")
        print("---------")
    elif x==3:
        print("Dice Rolled:")
        print("---------")
        print("|0      |")
        print("|   0   |")
        print("|      0|")
        print("---------")
    elif x==4:
        print("Dice Rolled:")
        print("---------")
        print("| 0   0 |")
        print("|       |")
        print("| 0   0 |")
        print("---------")
    elif x==5:
        print("Dice Rolled:")
        print("---------")
        print("| 0   0 |")
        print("|   0   |")
        print("| 0   0 |")
        print("---------")
    elif x==6:
        print("Dice Rolled:")
        print("---------")
        print("| 0 0 0 |")
        print("|       |")
        print("| 0 0 0 |")
        print("---------")
    else:
        print("Invalid number generated. Number higher than 6")
    z = input("\npress y to roll again or anything else to cancel\n")
