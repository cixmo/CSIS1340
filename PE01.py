import random

number = random.randint(0,100)
turn_count = 1
game_count = 0

print("\n\033[1mGuess the random number!\033[0m\nCorrectly guess a number from 0 to 100. The game will start over "
      "when you guess the correct number.\n")
while True:
    user_input = input("Choose a number between 0 to 100 ['q' to quit]: ")

    if user_input == 'q':
        print('\nGiving up so soon?\nThe correct number was',number,'and your play streak was',game_count,'games.')
        break
    elif user_input.isalpha():
        print(user_input, 'is not a valid response. Please use numbers instead.')
        continue
    else:
        user_input = int(user_input)

    if user_input < number:
        print('Your guess is too low. Please try again.')
        turn_count = turn_count + 1
        continue
    elif user_input > number:
        print('Your guess is too high. Please try again.')
        turn_count = turn_count + 1
        continue
    else:
        game_count = game_count + 1
        print('\n\033[1mCongratulations!\033[0m',number,'was the correct number.  It took',turn_count,
              'turns to figure out the answer and you have played',game_count,'games so far.')
        number = random.randint(0, 100)
        print('The game has been successfully reset.\n')
        turn_count = 1
        continue