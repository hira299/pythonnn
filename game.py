# import random

# def get_random_number(start, end):
#     """Generate a random number between start and end (inclusive)."""
#     return random.randint(start, end)

# def get_user_guess():
#     """Get the user's guess."""
#     guess = input("Enter your guess: ")
#     return int(guess)

# def check_guess(guess, correct_number):
#     """Check the user's guess against the correct number."""
#     if guess < correct_number:
#         return "Your guess is too low."
#     elif guess > correct_number:
#         return "Your guess is too high."
#     else:
#         return "Congratulations! You guessed it!"

# def play_game():
#     """Main function to play the number guessing game."""
#     print("Welcome to the Number Guessing Game!")
#     start = 1
#     end = 100
#     correct_number = get_random_number(start, end)
#     attempts = 0
#     max_attempts = 3

#     while attempts < max_attempts:
#         guess = get_user_guess()
#         attempts += 1
#         result = check_guess(guess, correct_number)
#         print(result)
        
#         if guess == correct_number:
#             print("You win!")
#             break
#     else:
#         print(f"You lose! The correct number was {correct_number}.")

# if __name__ == "__main__":
#     play_game()





'''capital guess'''

import random

# Dictionary of states and their capitals
capitals = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "California": "Sacramento",
    # Add more states and capitals as needed
}

# Convert dictionary keys to a list for random selection
states = list(capitals.keys())

# Track correct and incorrect responses
correct_answers = 0
incorrect_answers = 0

while True:
    # Randomly select a state from the list
    state = random.choice(states)
    
    # Prompt the user to guess the capital of the selected state
    print(f"What is the capital of {state}?")
    user_guess = input("Enter your guess: ").capitalize()  # Clean and format user input
    
    # Check if the guess is correct
    if user_guess == capitals[state]:
        print("Correct!")
        correct_answers += 1
    else:
        print(f"Incorrect. The capital of {state} is {capitals[state]}.")
        incorrect_answers += 1
    
    # Ask if the user wants to continue playing
    play_again = input("Do you want to continue? (yes/no): ").lower()
    if play_again != "yes":
        break

# Print total correct and incorrect responses
print(f"\nTotal Correct Answers: {correct_answers}")
print(f"Total Incorrect Answers: {incorrect_answers}")
