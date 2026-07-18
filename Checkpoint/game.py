import random
print("WELCOME TO THE GUESS THE NUMBER GAME")
z= int(random.randint (1,100))
print("-GUESS MY NUMBER -")


while 0<=z<=100 :
    y= int(input("Input your guess: "))
    if y<z : 
        print("Your guess is too low")
        breakpoint
    elif z<y :
        print("Your guess is too high") 
        breakpoint
    elif z==y :
        print("Your guess is right !!")
        break
