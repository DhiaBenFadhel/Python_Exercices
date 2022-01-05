name=input("Type your beautiful name here: ")
print ("Welcome",name,"to your adventure!")
deaths =0
Chest_O=0
while True:
    answer = input("Your on a road has come to an end,You can go left or right.Which way u wanna go? (L/R)or Q if u wanna quit:").lower()
    if answer=="l":
        answer=input("You come to a river, you can walk arround it or swim across (W/S):").lower()
        if answer=="w":
            print("You walked for too many kilometres and ran out of energy 😫 ! YOU DIED 😱 !")
            deaths += 1
            continue
        elif answer =="s":
            print("You swim across and you were eaten by the river monster 👾 ! YOU DIED 😱! ")
            deaths+=1
            continue
        else:
            print("Invalid Choice!,You loose!")
            break
    elif answer=="r":
        answer = input("You come to an old Bridge, it looks risky to across,You wanna go back or Continue (R/C):").lower()
        if answer=="r":
            print("You Pussy, there was a treasure chest on the end of the bridge but you missed it!")
            continue
        elif answer =="c":
            print("Nice!You reached the end of the bridge safe and you found a treasure chest 🤑 ,Good for you!")
            Chest_O+=1
            continue
        else:
            print("Invalid Choice!,You loose!")
            break
    elif answer =="q":
        print("Ok Take care adventurer ⚔  ")
        break
    else:
        print("Invalid Choice!,You loose!")
        break

print("GG man u completed the adventure with",Chest_O, "chests and with",deaths,"deaths")

