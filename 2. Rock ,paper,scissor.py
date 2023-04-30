import random
name=input("Enter your name:- ")
print(f"HELLO, {name} welcome to Rock Paper Scissor game! ")
print("In this game you have to choose one option either it is Rock ,Paper ,Scissor")
choice=["Rock","Paper","Scissor"]
x=random.choice(choice)
human = input("Enter your choice from Rock ,Paper ,Scissor-:")
if human=="Rock"and x=="Paper":
        print("Congratulation,you won the match")
elif human=="Paper"and x=="Rock":
        print("You lose the match")
if human == "Rock" and x == "Scissor":
        print("Congratulation,you won the match")
elif human=="Scissor" and x=="Rock":
        print("You lose the match")
if human==x:
        print("MATCH DRAW")