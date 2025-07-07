#Lab 5 - Manica Thea

#Task 1 
def cat_greeting(word):
    print(f'Cat says {word}')
    print('Cat says bonjour')

cat_greeting("Meow")

#Task 2
def generate_superhero_power():
    name = "Hazel"
    superpower = "Teleportation"
    print(f"{name}'s superpower is {superpower}!")

generate_superhero_power()

#Task 3 
def generate_superhero_power1():
    superpower = "Teleportation"
    return superpower

print(generate_superhero_power1())

#Task 4
def generate_superhero_power2(user_name, super_power):
    message = user_name + " has the power of " + super_power + "!"
    return message

print(generate_superhero_power2("Hazel", "Teleportation"))

#Task 5
def cat_greetings_loop():
    for i in range(5):
        print("Meow")

cat_greetings_loop()

#Task 6 
def generate_multiple_powers(powers_list):
    for power in powers_list:
        print(f"Superpower: {power}")

generate_multiple_powers(["Flying", "Telekinesis", "Super Strength" ])