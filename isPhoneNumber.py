import sys
def isPhoneNumber(text):
    if len(text) !=12:
        print("False!")
        sys.exit()
    if text[0:2].isdecimal():
        if text[3:4]=="-":
            if text[4:8].isdecimal():
                if text[8:9]=="-":
                    if text[9:13].isdecimal():
                        print("True!")
                    else:
                        print("False!")
                        sys.exit()
                else:
                    print("False!")
                    sys.exit()
            else:
                print("False!")
                sys.exit()
        else:
            print("False!")
            sys.exit()
    else:
        print("False!")
        sys.exit()
    return(text)
isPhoneNumber('111-1111-22')
        