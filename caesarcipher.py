import pyperclip, sys
SYMBOL = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def translate(Secretnum, messenger):
            mess= ''
            for i in messenger:
                if i in SYMBOL:
                    num  = int(SYMBOL.find(i))
                    num = num + Secretnum

                    if num > len(SYMBOL):
                        num = num - len(SYMBOL)
                        mess = mess + SYMBOL[num]    
                else:
                    mess = mess + i
            print(mess)
            return mess
def untranslate(Secretnum, messenger):
            mess= ''
            for i in messenger:
                if i in SYMBOL:
                    num  = SYMBOL.find(i)
                    num = num - Secretnum

                    if num < len(SYMBOL):
                        num = num + len(SYMBOL)
                        mess = mess + SYMBOL[num]    
                else:
                    mess = mess + i
            print(mess)
            return mess
def main():
    print("""Caesar Cipher, by Lê Công Bình lecongbinh37@gmail.com
    The Caesar translate is a shift untranslate that uses addition and subtraction
    to encrypt and decrypt letters.""")
    while True:
        print("Lựa chọn chế độ bạn muốn sử dụng (translate or untranslate).\nHoặc nhập Quit để thoát chương trình.\n")     
        mode= input("> : ")
        if  mode.lower().startswith("q"):
            sys.exit()
        print("Bạn đã chọn chế độ {}".format(mode))
        print("Vui lòng nhập số bí mật để chương trình cài đặt.")
        Secretnum = int(input("Secretnum : "))
        print("Nhập văn bản để thực hiện tạc vụ")
        messenge = input("Messenger : ")
        messenger = messenge.upper()
        if mode == "TRANSLATE":
            translate(Secretnum, messenger)
        if mode == "UNTRANSLATE":
            untranslate(Secretnum, messenger)
        
        
        
if __name__ == "__main__":
    main()

