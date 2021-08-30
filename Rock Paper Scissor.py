import random
import time

print("Welcome to Rock Paper Scissor game! This is developed by Virat Chauhan.")
print("Hope you know all the basic rules of this game.\n"
"You will battle 10 times against the Computer and the result will declared on the basis of BEST OUT OF 10.")
time.sleep(3)
print("\nLet's get started!")
time.sleep(1)

rounds = 0
pc_won = 0
user_won = 0

def results():
    time.sleep(1)
    print("\nThat was a nice match! 10 rounds are over!")
    print(f"You won {user_won} rounds!\nPC won {pc_won} rounds!\n")
    if user_won>pc_won:
        print("Congratulations! You won the match!")
    elif user_won==pc_won:
        print("You & PC both won equal amount of rounds. So it's a TIE!")
    else:
        print("Sorry you lost the match! Better luck next time!")

while rounds<12: #ignore the fact that i choosed 12 rounds here instead of 10!
    user_move = input("\nChoose your moves (Rock, Paper, Scissor):\n> ")
    pc_move = random.choice(["rock", "paper", "scissor"])
    if user_move=='rock' and pc_move=='scissor': #win
        print(f"You choosed {user_move}!\nPC choosed {pc_move}!")
        print("You breaked the scissor and won this round!")
        rounds+=1
        user_won+=1
    elif user_move=='paper' and pc_move=='rock': #win
        print(f"You choosed {user_move}!\nPC choosed {pc_move}!")
        print("You snatched the rock and won this round!")
        rounds+=1
        user_won+=1
    elif user_move=='scissor' and pc_move=='paper': #win
        print(f"You choosed {user_move}!\nPC choosed {pc_move}!")
        print("You teared the paper and won this round!")
        rounds+=1
        user_won+=1
    elif user_move=='rock' and pc_move=='paper': #lose
        print(f"You choosed {user_move}!\nPC choosed {pc_move}!")
        print("PC snatched your rock and won this round!")
        rounds+=1
        pc_won+=1
    elif user_move=='paper' and pc_move=='scissor': #lose
        print(f"You choosed {user_move}!\nPC choosed {pc_move}!")
        print("PC teared your paper and won this round!")
        rounds+=1
        pc_won+=1
    elif user_move=='scissor' and pc_move=='rock': #lose
        print(f"You choosed {user_move}!\nPC choosed {pc_move}!")
        print("PC breaked your scissor and won this round!")
        rounds+=1
        pc_won+=1
    elif user_move==pc_move:
        print(f"You choosed {user_move}!\nPC choosed {pc_move}")
        print("Both users choosed same move. It's a tie! No one gets any points.")
        rounds+=1
    else:
        print("That was an invalid move. Please try again!")
    if rounds>=10:
        results()
        break