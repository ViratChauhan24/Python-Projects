import random
print("Welcome to Guess the number. This is developed by Virat Chauhan.\n"
"\nHow to play?\n"
" Objective is to guess the actual number by entering diffrent numbers each time.\n"
" Program will reply to the number which you have entered - either it is smaller or higher in value to the actual number.\n"
" Think & guess the correct number.\n"
" You have only 9 guesses. So best of luck!")
num = random.randint(0,50)
game_loop = True
guess = 0
max_guess = 9
while game_loop:
    inp = int(input("\nGuess the number: "))
    guess += 1
    max_guess -= 1
    if inp > num:
        print("Your number is greater than the actual number.")
        print(f"You have now {max_guess} guesses left!")
        if max_guess == 0:
            print("Sorry your all guesses are exhuasted. You lost! Better luck next time!")
            game_loop = False
    elif inp < num:
        print("Your number is smaller than the actual number.")
        print(f"You have now {max_guess} guesses left!")
        if max_guess == 0:
            print("\nSorry, all of your guesses are now exhuasted. You lost! Better luck next time!")
            print("The number was", num)
            game_loop = False
    elif inp == num:
        print("Congratulations! you have successfully guessed the correct number.")
        print(f"You guessed it in {guess} turns!")
        game_loop = False