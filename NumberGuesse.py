import random

print("^^^^^Welcome To GUESSNUMBER GAME 🔥🔥🔥^^^^^ ")

num_given=int(input("Type a number: "))

if num_given <=0:
    print("Please enter a number bigger than zero: ")
    quit()

random_number = random.randint(0, num_given)
trys=0
while True:
    user_guess =int(input("Make a guess: "))
    if user_guess == random_number:
        print("U got it! 👏 " )
        trys+=1
        break
    elif user_guess >random_number:
        print("Nope😢,U are above the number,Try again😔")
    else:
        print("Nope😢,U are below the number,Try again😔")
        trys+=1
if trys == 1:
    print("Well done, you guessed it out in", trys,"trys😲")
else:
    print("You guessed it out in ", trys," trys 🐢 ")
