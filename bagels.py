
import random

NUM_DIGITS = 3  # (!) Try setting this to 1 or 10.
MAX_GUESSES = 10  # (!) Try setting this to 1 or 100.

def main():
    print('''Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython.com

I am thinking of a {}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
When I say:    That means:
Pico         One digit is correct but in the wrong position.
Fermi        One digit is correct and in the right position.
Bagels       No digit is correct.
 
For example, if the secret number was 248 and your guess was 843, the
clues would be Fermi Pico.'''.format(NUM_DIGITS))
    while True:
        Secretnum = getSecretnum()
        numGuess = 1
        guess = ''
        while numGuess <= MAX_GUESSES:
            print("Lần đoán số {}".format(numGuess))
            guess = input("Nhập số bạn muốn đoán: ")
            numGuess += 1
            clues = getClues(Secretnum, guess)
            print(clues)
            if Secretnum == guess:
                print("You got it!")
                break
            if numGuess > MAX_GUESSES:
                print("Số bạn cần đoán là: ",Secretnum)
                break
        print("Bạn có muốn chơi tiếp không?")
        if input().lower().startswith("y"):
            main()
        else:
            break
def getSecretnum():
    numbers = list('0123456789')
    random.shuffle(numbers)
    Secretnum = ''
    for i in range(NUM_DIGITS):
        Secretnum += str(numbers[i])
    return Secretnum
def getClues(Secretnum, guess):
    clues = []
    if guess == Secretnum:
        print("Yoy got it!")
    for i in range(NUM_DIGITS):
        if guess[i]==Secretnum[i]:
            clues.append("Pico")
        elif guess[i] in Secretnum:
            clues.append("Fermi")
    if len(clues) == 0:
        clues.append("Bagels")
    else:
        clues.sort()
    return clues
if __name__ == '__main__':
    main()