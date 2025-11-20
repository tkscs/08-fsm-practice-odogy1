x = 0
y = 0
a = 0
while x == 0:
    a = 0
    axe = input("Do you want an item? (1/n)")
    if axe == "n":
        print("Bye!")
        x = 1
    elif axe == "1":
        y = y + 1
        while a == 0:
            ask = input(f"Do you want an {y} coin item? (y/n/1)")
            if ask == "n":
                y = 0
                print("Bye!")
                a = 1
            elif ask == "y":
                print(f"Here's your {y} coin item!")
                a = 1
            elif ask == "1":
                y = y + 1