from ast import While
import decimal
from queue import PriorityQueue
import random, sys
from webbrowser import get
maxBet = 1000
# Xem character map
HEART = chr(9829)       # tạo biểu tượng chất CƠ
DIAMONDS = chr(9830)    # Tạo biểu tượng chẩ RÔ
SPADES = chr(9824)      # Tạo biểu tượng chất Bích
CLUBS = chr(9827)       # Tạo biểu tượng chất chuồn
CHAT = [HEART, DIAMONDS, SPADES, CLUBS]
def getDeck():
    bo = []
    for i in range(2,11):
        for chat in CHAT:
            bo.append((i,chat))
    for chat in CHAT:
        for x in ["A", "J", "Q", "K"]:
            bo.append((x, chat))
    random.shuffle(bo)
    return bo
def getBet(maxBet):
    """Ask the player how much they want to bet for this round."""
    while True:  
        print('How much do you bet? (1-{}, or QUIT)'.format(maxBet))
        bet = input('> ').upper().strip()
        if bet == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        if not bet.isdecimal():
            continue  
        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet 
def display(player, computers):
    if computers:
        print("Computer: ")
        rows = ["","","","",""]
        rows[0] += " _____ "*3
        for computer in computers :
            i,chat = computer
            i= str(i)
            rows[1] += ("|{}    |".format(i))
            rows[2] += ("|  {}  |".format(chat))
            rows[3] += ("|___ {}|".format(i))
        for i in range(5):
            print(rows[i])
    if player:
        print("Player: ")
        rows = ["","","","",""]
        rows[0] += " _____ "*3
        for computer in player :
            i,chat = computer
            i= str(i)
            rows[1] += ("|{}    |".format(i))
            rows[2] += ("|  {}  |".format(chat))
            rows[3] += ("|___ {}|".format(i))
        for i in range(5):
            print(rows[i])
    return print()
def getValues(bai):
    Value = 0
    for computer in bai:
        i, chat = computer
        if i =="K":
            Value += 13
        elif i == "A":
            Value += 1
        elif i == "J":
            Value+= 11
        elif i =="Q":
            Value+=12
        else:
            Value += i
    while Value > 10:
        Value -=10
    return Value


def main():
    money = 5000
    print("""
    Luật chơi:
    Bạn sẽ được chia 3 quân bài, sau khi nhận quân bạn sẽ đặt cược.
    Mức cược tối đa là $1000 và tối thiểu là $100.
    Tổng 3 quân bài sẽ được quy về mười, nếu lớn hơn 10, 
    sẽ lần lượt trừ đi 10 để khi nào được số bé thua hoặc bằng 10.
    """)
    while True:
        print("Đến lượt bạn đặt cược!")
        print("Money: ", money)
        print("Nhập số tiền cược hoặc Quit để thoát.")
        bet = getBet(maxBet)
        print("Bet : ", bet)
        bo = getDeck()
        computers = [bo.pop(), bo.pop(), bo.pop()]
        player = [bo.pop(), bo.pop(), bo.pop()]
        print(display(computers, player))
        Comp = getValues(computers)
        print("Computer = ", Comp)
        Play = getValues(player)
        print("Player = ",Play)
        if Comp > Play:
            money -= bet
            print("You lost!")
        elif Comp < Play:
            money += bet
            print("You win!")
        else:
            print("Draw!")
if __name__ == "__main__":
    main()

    
