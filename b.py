import random
Num_digits = 3
Num_Guessmax = 10
def main():
    print("""
    Đoán một số gồm 3 chữ số.
    Bạn có tối đa 10 lượt đoán
""")
    while True:
        guess= ''
        numguess = 1
        NumSecret = get_Numsecret()
        print(get_Numsecret())
        print('Lần đoán số {}'.format(numguess))
        while numguess <= Num_Guessmax:
            guess = ''
             # Keep looping until they enter a valid guess:
            while len(guess) != Num_digits or not guess.isdecimal():
                    print('Guess #{}: '.format(numguess))
                    guess = input('> ')
            clues = get_clues(guess, get_Numsecret())
            print(clues)
            numguess += 1
            if guess == NumSecret:
                #clues = get_clues()
                    print("Bạn đã đoán đúng.")
                    print("Số máy tính random là: ",NumSecret)
                    print("Bạn đã đoán đúng trong {}\n".format(numguess))
                    break
            elif numguess > Num_Guessmax:
                print("Bạn đã sử dụng hết số lượt chơi của mình.")
                print("Số bạn cần đoán là {}".format(NumSecret))
        print("Bạn có muốn chơi lại không.(Yes or No): ")
        if not input().lower().startswith("y"):
            break
            
def get_Numsecret():
    number= list("0123456789")
    NumSecret =""
    random.shuffle(number)
    for i in range(Num_digits):
        NumSecret += str(number[i])
    return NumSecret
def get_clues(guess , NumSecret):
    if guess == NumSecret:
        return("Bạn đã đoán đúng")
    clues = []
     
    for i in range(Num_digits):
        if guess[i] == NumSecret[i]:
            clues.append("Location ")
        elif guess[i] in NumSecret:
            clues.append("Inlocation ")
    if len(clues)==0:
        return "Sai"
    else:
        clues.sort()
        return " ".join(clues)
    
#get_Numsecret()
if __name__ == '__main__':
    main()
