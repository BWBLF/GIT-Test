#nhap lua chon cua ban 
from random import randint  #lay tu thu vien ham random va xuat ra ham randint
print ("Nhap Dam, La or Keo:")
players = input()
print ("you select: " + players + "!")
b = randint(0,2) #random ra 1 so 0 hoac 1 hoac 2
if b == 1: 
    computer = "Keo"
if b == 0:
    computer = "Dam"
if b == 2:
    computer = "La"
print ("Computer select: " + computer)
if players == "Dam":
    if computer == "Dam":
        print ("Draw!")
    if computer == "La":
        print ("You Lose!")
    if computer == "Keo":
        print ("You Win!")
if players == "La":
    if computer == "La":
        print ("Draw!")
    if computer == "Keo":
        print ("You Lose!")
    if computer == "Dam" :
        print ("You Win!")
if players == "Keo":
    if computer == "Keo!":
        print ("Draw")
    if computer == "Dam":
        print ("You Lose!")
    if computer == "La":
        print ("You Win!")
