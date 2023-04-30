import random
import time
print("Welcome Let's play the game")
name=input("What is your name? : ")
age=input("What is your age? : ")
Attempts=int(input("How many times You want to roll set of dices? : "))
for i in range(Attempts):
  dice_1=random.randrange(1,7)
  dice_2=random.randrange(1,7)
  time.sleep(1)
  print(f"{name} your dice have the following numbers: ",dice_1,dice_2)