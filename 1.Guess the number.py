import random
start=int(input("enter the starting range:- "))
end=int(input("enter the end range:- "))
x = random.randint(start,end)
c = 0
while True:
    c += 1
    guess = int(input("Guess a number:- "))
    if x == guess:
        print("Congratulations you did it in", c, "tries!")
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You Guessed too high!")
            
        
             
