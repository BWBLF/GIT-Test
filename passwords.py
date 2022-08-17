while True:
    a= input('Nhap ten cua ban:')
    print(a)
    if a == 'Binh':
        print('Xin chao, Vui long nhap mat khau?')
        while True:
            b = input()
            if b== 'Ban':
                print("Da dang nhap")
                break
            elif b != "Ban":
                print("Vui long nhap lai MK")
        if b == "Ban":
            break
        elif b != "Ban":    
            print("Mat khau sai. Vui long nhap lai mat khau: ")
            continue
    elif a != "Binh":
        print("Vui long nhập tên của bạn!")
        continue