import random
EASY_LEVEL_ATTEMPT = 10
HARD_LEVEL_ATTEMPT = 5
def set_difficulty(level_choosen):
    if level_choosen == 'easy':
       return EASY_LEVEL_ATTEMPT
    else:
        return HARD_LEVEL_ATTEMPT

def check_answer(guessed_number,answer,attempts):
    if guessed_number<answer:
        print("Your guess is too low")
        return attempts-1
    elif guessed_number>answer:
        print("Your guess is too high")
        return attempts-1
    else:
        print(f"Your guess is correct ... The answer was {answer}")

def game():
    print("Let me think of a number from 1 to 50")
    answer = random.randint(1,50)
    level = input("Choose difficulty level.....Type 'easy' or 'hard' : ")
    attempts = set_difficulty(level)
    guessed_number=0
    while(guessed_number!= answer):
        print(f'You have {attempts} remaining to guess the number')
        guessed_number = int(input('Guess the number: '))
        attempts=check_answer(guessed_number,answer,attempts)
        if attempts == 0:
            print("You have no attempts..you loose the game !")
            return 
        elif guessed_number != answer:
            print("Guess again ")
game()