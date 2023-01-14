import random as rand
number= rand.randint(1,100)
guess=int(input("guress the number"))



while guess != number:
    if guess > number:
        print("the number is grrrrret")
    else:
        print("too low")
        guess = int(input())
print ("wont the game")