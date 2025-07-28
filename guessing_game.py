#Guessing Game - Manica Thea 

#Step 2 Import the random so we can pick random number
import random 

def generate_random_number():
    """
    Pick and return a random number between 1 and 100.
    """
    return random.randint(1, 100)

#Step 3 Asks the user to guess a number
def get_user_guess(): 
    """
    Keep asking the user to type a number from 1 to 100.
    """
    while True:
        try:
            guess = int(input("Enter a number between 1 and 100: "))
            if guess >= 1 and guess <= 100:
                return guess
            else:
                print("Enter a valid number between 1 and 100.")
            
        except ValueError:
            print("Invalid Input, please enter a valid number")


#Step 4 The main game function
def play_guessing_game():
    """
    This starts the game and picks a secret number.
    Then it keeps asking the player to guess until they get it right.
    It tells the player if their guess is too high or too low and counts how many guesses the player took.
    """
    
    print("Welcome to the Guessing Game!")
    secret_number = generate_random_number() #Pick a number for the player to guess
    attempts = 0 #Keep track of how many guesses

    while True:
        guess = get_user_guess() #Ask player for a guess
        attempts += 1 #Add one to guesses

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too High! Try again.")
        else:
            print(f"Congratulations! You guessed it in {attempts} attempts.")
            break #End the game when the player guessed the right number
        
        
#Step 5 Keeps playing the game until the player wants to stop
def game_loop():
    while True:
        play_guessing_game()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye!")
            break #Stops playing if the player says no

#Step 6 This makes sure the game starts when you run the file
if __name__ == "__main__":
    game_loop()

