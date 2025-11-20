# write code to implement a turnstile

x = 0

state = "locked"

while x == 0:
    response = input("Enter a coin(c) or push(p).")

    if state == "locked":
        if response == "c":
            state = "unlocked"
        elif response == "p":
            print("You may not pass.")
    elif state == "unlocked":
        if response == "c":
            print("I'm greedy.")
        elif response == "p":
            state = "locked"
    print(state)



