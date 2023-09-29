#Guess the number Computer 

import random

random_number=random.randint(1,10)
guess=int(input("Please write a number between 1 and 10: "))

print("You only have three opportunities to guess the number")
print("/n", random_number)
i=2
while i>0:

	if guess==random_number:
		print("congratulations you won")
		i=0
	elif guess>random_number:
		print("Write a smaller number ")
		guess=int(input("Please write a number between 1 and 10: "))
		i=i-1
		if i==0:
			print("YOu loosEEer")
	elif guess<random_number:
		print("Write a bigger number ")
		guess=int(input("Please write a number between 1 and 10: "))
		i=i-1
		if i==0:
			print("YOu loosEEer")
