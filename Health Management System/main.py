import time
import datetime

def main_inp():
    global File_Response
    global user_input
    print("Welcome to Health Management System!\nThis is developed by Virat Chauhan to keep your daily diet & exercises record.")
    time.sleep(2)
    File_Response = input("\nWhat do you want to open/edit? Reply with 1 for Diet report or 2 for Exercises report!\n> ")
    user_input = input("To view your record reply with 1, to write your today's report reply with 2.\n> ")

main_inp()

if File_Response == '1' and user_input == '1':
    #Diet View
    View_NameResponse = input("To retrieve your past record, Continue with entering your name!\n> ")
    if View_NameResponse=='Harry' or 'harry' or 'HARRY':
        f = open("Health Management System\Harry_Diet.txt")
        content = f.read()
        print(content)
        f.close()
    elif View_NameResponse=='Rohan' or 'rohan' or 'ROHAN':
        f = open("Health Management System\Rohan_Diet.txt")  
        content = f.read()
        print(content)
        f.close()
    elif View_NameResponse=='Kappa' or 'kappa' or 'KAPPA':
        f = open("Health Management System\Kappa_Diet.txt")
        content = f.read()
        print(content)
        f.close()
elif File_Response == '1' and user_input == '2':
    #Diet Edit
    Edit_NameResponse = input("To write your today's report, Continue with entering your name!\n> ")
    if Edit_NameResponse=='Harry' or 'harry' or 'HARRY':
        f = open("Health Management System\Harry_Diet.txt", "a")
        diet_input = input("\nEnter your today's diet routine:\n> ")
        f.write(f"\n[{datetime.datetime.now()}] {diet_input}")
        f.close()
    elif Edit_NameResponse=='Rohan' or 'rohan' or 'ROHAN':
        f = open("Health Management System\Rohan_Diet.txt", "a")
        diet_input = input("\nEnter your today's diet routine:\n> ")
        f.write(f"\n[{datetime.datetime.now()}] {diet_input}")
        f.close()
    elif Edit_NameResponse=='Kappa' or 'kappa' or 'KAPPA':
        f = open("Health Management System\Kappa_Diet.txt", "a")
        diet_input = input("\nEnter your today's diet routine:\n> ")
        f.write(f"\n[{datetime.datetime.now()}] {diet_input}")
        f.close()
elif File_Response == '2' and user_input == '1':
    #Ex View
    View_NameResponse = input("To retrieve your past record, Continue with entering your name!\n> ")
    if View_NameResponse=='Harry' or 'harry' or 'HARRY':
        f = open("Health Management System\Harry_ex.txt")
        content = f.read()
        print(content)
        f.close()
    elif View_NameResponse=='Rohan' or 'rohan' or 'ROHAN':
        f = open("Health Management System\Rohan_ex.txt")  
        content = f.read()
        print(content)
        f.close()
    elif View_NameResponse=='Kappa' or 'kappa' or 'KAPPA':
        f = open("Health Management System\Kappa_ex.txt")
        content = f.read()
        print(content)
        f.close()
elif File_Response == '2' and user_input == '2':
    #Ex Edit
    Edit_NameResponse = input("To write your today's report, Continue with entering your name!\n> ")
    if Edit_NameResponse=='Harry' or 'harry' or 'HARRY':
        f = open("Health Management System\Harry_ex.txt", "a")
        ex_input = input("\nEnter your today's exercise routine:\n> ")
        f.write(f"\n[{datetime.datetime.now()}] {ex_input}")
        f.close()
    elif Edit_NameResponse=='Rohan' or 'rohan' or 'ROHAN':
        f = open("Health Management System\Rohan_ex.txt", "a")
        ex_input = input("\nEnter your today's exercise routine:\n> ")
        f.write(f"\n[{datetime.datetime.now()}] {ex_input}")
        f.close()
    elif Edit_NameResponse=='Kappa' or 'kappa' or 'KAPPA':
        f = open("Health Management System\Kappa_ex.txt", "a")
        ex_input = input("\nEnter your today's exercise routine:\n> ")
        f.write(f"\n[{datetime.datetime.now()}] {ex_input}")
        f.close()
else:
    print("You gave invalid input! The program will now restart. Please try again!\n")
    time.sleep(2)
    main_inp()