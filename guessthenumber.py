from random import randint

HARD_LEVEL = 5
EASY_LEVEL = 10

"""
this is small guess the randowm number game designed on binary search algorithm.
"""

def get_attempts():
    """
        return number of attemtps depending on what user has oppted
    """
    difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard':").lower()
    if difficulty_level == 'easy':
        return EASY_LEVEL
    else:
        return HARD_LEVEL


def check_answer(user_number, number_to_guess):
    """
        prints if number is lowor high thatn guessed number and return True if guessed number is same as user entered number, else return False
    """
    if user_number < number_to_guess:
        print("Too Low !!")
        return False
    elif user_number > number_to_guess:
        print("Too High !!")
        return False
    else:
        return True



def game():
    game_over = False
    user_guess_number = 0
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number_of_attempts = get_attempts()
    number_to_guess = randint(1, 100)
    print(number_to_guess)
    while not game_over:
        print(f"You have {number_of_attempts} attempts remaining to guess the number.")
        user_guess_number = int(input("Make a guess ! : \n"))
        result = check_answer(user_guess_number, number_to_guess)
        if result:
            number_of_attempts = 0
            print("You guessed it !!!")
        else:
            number_of_attempts = number_of_attempts - 1

        if number_of_attempts == 0:
            print("Game Over --------------------!!!")
            game_over = True
        else:
            print("Guess Again !!")


game()
