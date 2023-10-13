#Gues the number (user secret)
import random

secret_number=int(input("Elige un numero random entre 1 y 10: "))

guess=random.randint(1,10)

i=3
while i>0:
    if secret_number==guess:
        print(guess)
        i==0
        print("ese mero")
    elif secret_number != guess:
        print(guess)
        print("este no es")
        i=i-1
        guess=random.randint(1,10)
        