import random

guess_count = 0
game_exit = ''
rand_num = random.randint(1, 9)

while game_exit != 'exit':
    user_guess = input('Guess a number between 1 and 9:\n')
    if user_guess.isdigit() and 10 > int(user_guess) > 0:
        user_guess = int(user_guess)
    else:
        invalid_exclamations = [1, 2, 3, 4, 5]
        choice = random.choice(invalid_exclamations)
        if choice == 1:
            print('Invalid Entry. Guess again muthaf-----!')
        elif choice == 2:
            print('damn bro that wasn\'t a valid numbah. guess again.')
        elif choice == 3:
            print('Whoa lets all just calm down and choose a valid number.')
        elif choice == 4:
            print('Yo. Calm yo ass down and choose a valid number.')
        elif choice == 5:
            print('No.')
        continue

    guess_count += 1
    if user_guess == rand_num:
        print('Congratulations you guessed it exactly right!')
        print('Guess count: {}'.format(guess_count))
        guess_count = 0
        rand_num = random.randint(1, 9)
        game_exit = input('Press enter to play again. Type "exit" to quit.\n').lower()
    elif user_guess > rand_num:
        print('Too high')
    elif user_guess < rand_num:
        print('Too low')
    else:
        print('Something went wrong. Please try again.')
print('Thanks for playing!')