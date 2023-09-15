#string concatenation

#Madlibs game

#It is a game where you will receive 10 different words, to which you will be creating a story
#You will ahve to make a sentence that make sense for each word. 

#In this part we make introduction to the game
print("Hello welcome to Madlibs")
print("Instructions:")
print("For this game you will receive 10 words from the list ")
print("For which you will have to make a short story that makes sense")
print("The word will be added to the end of your sentence")

#We call the random library 
import random


#We start coding here

#Opening the file in the read mode
file = open("words.txt", "r")

#reading the file
data=file.read()

#making the data into a list
word_list=data.split("\n")




i=0
a=[]
b=[]
while i <11:
	n=random.randint(0,999)
	a.append(word_list[n])
	print(a[i])
	b.append(input("write your short sentence: ")+" " + a[i])
	print(b)

	i=i+1


print(b)



	