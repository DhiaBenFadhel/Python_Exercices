print("*-*-*-*-Welcome to QuizGame!-*-*-*-*")

playing = input("Do u wanna play? (y/n): ")

if playing.lower() != "y":
    quit()

print("Yeeees LESGOO ;) ")
score=0
print("1/What does GPU stand for? ")
answer = input("Answer here: ")
if answer.lower() == "graphic processing unit":
    print("NOICE :) ")
    score+=1
else:
    print("NOPE!!")
print("2/What does CPU stand for? ")
answer = input("Answer here: ")
if answer.lower() == "central processing unit":
    print("NOICE :) ")
    score+=1
else:
    print("NOPE!!")
print("3/What does PSU stand for? ")
answer = input("Answer here: ")
if answer.lower() == "power supply unit":
    print("NOICE :) ")
    score+=1
else:
    print("NOPE!!")
print("4/What does RAM stand for? ")
answer = input("Answer here: ")
if answer.lower() == "random access memory":
    print("NOICE :) ")
    score+=1
else:
    print("NOPE!!")
print ("your score is " ,score)
print ("you got ",(score/4)*100,"%.")