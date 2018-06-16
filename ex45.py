from random import randint
random = randint(1, 99)
UI = int(input("Enter an integer from 1 to 99:"))
while UI != random:
    if UI > random:
        print("guess is high")
        UI = int(input("Enter an integer from 1 to 99: "))

    elif UI < random:
        print("guess is low")
        UI = int(input("Enter an integer form 1 to 99: "))

    else:
        print("You guessed it!")
        break



