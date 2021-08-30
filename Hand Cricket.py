# This project isn't completed yet, so better read the whole code, understand it & play according to what feature is available and what isn't.

import random
import time
print("Welcome to Hand Cricket. This is developed by Virat Chauhan. \n"
"Let's get started! Hope you know basic rules of this game.")
time.sleep(3)

pc_out = False
user_total = 0
pc_total = 0
total_balls = 0

def bat_1():
    print("\n1st Inning starts.\nYou are Batting\nand PC is Bowling")
    while (True):
        global user_total
        global total_balls
        user_move = int(input("\nChoose your Moves: "))
        user_total = user_total + user_move
        pc_move = random.randint(1,6)
        if user_move==pc_move:
            print("PC's Move - ", pc_move)
            print("You was BOLD!\n"
            "Now it's turn for PC to Bat.\n"
            f"You scored {user_total}!\n"
            "Second Inning starting in 3 Seconds.")
            time.sleep(3)
            total_balls = 0
            bowl_2()
        elif user_move!=pc_move:
            total_balls = total_balls + 1
            time.sleep(0.5)
            print(f"PC's Move - {pc_move} \nTotal Score - {user_total} \nin {total_balls} Ball(s)")

# def bat_2():

# def bowl_1():

def bowl_2():
    print("\n2nd Inning starts.\nYou are Bowling\nand PC is Batting\nTarget:", user_total+1,)
    while (True):
        global pc_total
        global pc_move
        global total_balls
        user_move = int(input("\nChoose your Moves: "))
        pc_move = random.randint(1,6)
        pc_total = pc_total + pc_move
        if user_move==pc_move and pc_total<user_total:
            print("PC's Move - ", pc_move)
            print("PC was BOLD!"
            "\nYou won the match by", user_total-pc_total, "runs")
            exit()
        elif pc_total>user_total:
            print("PC's Move - ", pc_move)
            print(f"in {total_balls} Ball(s)")
            print("PC won the Match!")
            exit()
        elif user_move!=pc_move:
            total_balls = total_balls + 1
            time.sleep(0.5)
            print(f"PC's Move - {pc_move} \nTotal Score - {pc_total} \nin {total_balls} Ball(s)\nTarget - {user_total+1}")

toss_winlose_list = (["toss_lose", "toss_win"])

def toss():
    print("\nIt's time for toss!")
    toss_input = input("Choose your call: HEAD or TAIL\n> ")

    if toss_input == 'Head' or 'HEAD' or 'head': # Lmfao, i know i could have used.lower() func, but i am lazi af!
        toss_do = (random.choice(toss_winlose_list))

        if toss_do == ('toss_lose'):
            toss_losechoice = (random.choice(["BAT", "BOWL"]))
            print("Computer won the toss and decided to", toss_losechoice,"first!")

            if toss_losechoice == 'BAT':
                print("Bat test")
            else:
                print("Bowl test") #bowl()

        elif toss_do == ('toss_win'):
            toss_winchoice = input("You won the toss! What do you want to choose first? BAT or BOWL\n> ")

            if toss_winchoice == 'bat' or 'BAT' or 'Bat':
                bat_1()
            elif toss_winchoice == 'bowl' or 'BOWL' or 'Bowl':
                print("Bowl Test") # bowl()

    elif toss_input == Tail or TAIL or tail:
           toss_do = random.choices('toss_win', 'toss_lose')

           if toss_do == 'toss_lose':
               toss_losechoice = random.choices('BAT', 'BOWL')
               print("Computer won the toss and decided to", toss_losechoice,"first!")

               if toss_losechoice == 'BAT':
                bat()
               else:
                bowl()

           elif toss_do == 'toss_win':
            toss_winchoice = input("You won the toss! What do you want to choose first? BAT or BOWL\n> ")

            if toss_winchoice == bat or BAT or Bat:
                bat_1()
            elif toss_winchoice == bowl or BOWL or Bowl:
                bowl()

toss()
