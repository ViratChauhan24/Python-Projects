def calculator():
 print ("\n Welcome to Faulty Calculator: This is developed by Virat Chauhan\n")
 operation = input("  Please enter the following operation you would like to complete\n"
 "   + for addition\n"
 "   - for substraction\n"
 "   * for multiplication\n"
 "   / for division\n"
 
 "\n  Enter your choice: ")
 
 num1 = int(input("  Enter your first number: "))
 num2 = int(input("  Enter your second number: "))

 #56+9=77, 45*3=555 & 56/6=4
 
 if operation=='+':
     if num1==56 and num2==9:
         print(f"\n  {num1} + {num2} = 77")
     else:
         print(f"\n  {num1} + {num2} = {num1 + num2}")
 elif operation=='-':
     print(f"\n  {num1} - {num2} = {num1 - num2}")
 elif operation=='*':
     if num1==45 and num2==3:
         print(f"\n  {num1} * {num2} = 555")
     else:
         print(f"\n  {num1} * {num2} = {num1 * num2}")
 elif operation=='/':
     if num1==56 and num2==6:
         print(f"\n  {num1} / {num2} = 4")
     else:
         print(f"\n  {num1} / {num2} = {num1 / num2}")
 else:
     print("\n  You entered a invalid operator!")
 again()

def again():
 print("\n Do you want to use the calculator again?")
 again = input(" Please type y for YES or n for NO: ")
 
 if again=='y':
     calculator()
 elif again=='n':
     print("\nSee you later!")
 else:
     again()

calculator()