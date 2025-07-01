#Lab 4 - Manica Thea

#Task 1 
checking = "yes"

while checking == "yes":
    print("What is your age?: ")
    user_input = input()
    if int(user_input) >= 18:
        print("Yes you can vote")
    else: 
        print("You can't vote")
    print("Would you like to check another age?")
    user_input2 = input()
    checking = user_input2

#Task 2
list1 = [10, -12, 4, 0, -7]

for x in list1:
    if x > 0:
        print("Value is positive")
    elif x < 0:
        print("Value is negative")
    elif x == 0:
        print("Number is zero")

#Task 3 
inventory = ["coal", "wood", "obsidian", "sand", "diamonds"]

for i in range(len(inventory)):
    block = inventory [i]
    print("You found: " + block)
    if block == "diamonds":
        print("Jackpot!")
        break