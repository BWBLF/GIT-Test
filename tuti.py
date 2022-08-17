import random
'Kéo' == 1
"Búa" == 2
"Giấy" == 3
win = 0
loss = 0
hoa = 0
comp = random.randint(1,3)
while True:
    you = input("Nhập lựa chọn của bạn Búa, Kéo hoặc Giấy: ")
    if you != "Kéo" and you != "Búa" and you != "Giấy":
        print("Vui lòng nhập lại lựa chọn của bạn!")
    elif you == "Kéo":
        if comp == 1:
            print("Lựa chọn của Computer là: Kéo ")
            print("Hòa!\n Bạn có muốn chơi tiếp không!")
            hoa += 1
            print("Thành tích của bạn là:","\nThắng:",win,"\nHòa:",hoa,"\nThua:",loss )
            a = input("Có hoặc Không!")
            print()
            if a== "Có":
                continue
            elif a == "Không":
                break
        if comp == 2:
            print("Lựa chọn của Computer là: Búa ")
            print("Bạn Thua!\n Bạn có muốn chơi tiếp không!")
            loss += 1
            print("Thành tích của bạn là:","\nThắng:",win,"\nHòa:",hoa,"\nThua:",loss )
            a = input("Có hoặc Không!")
            if a== "Có":
                continue
            elif a == "Không":
                break
        if comp == 3:
            print("Lựa chọn của Computer là: Giấy ")
            print("Bạn Thắng!\n Bạn có muốn chơi tiếp không!")
            win += 1
            print("Thành tích của bạn là:","\nThắng:",win,"\nHòa:",hoa,"\nThua:",loss )
            a = input("Có hoặc Không!")
            if a== "Có":
                continue
            elif a == "Không":
                break

    elif you == "Búa":
        if comp == 1:
            print("Lựa chọn của Computer là: Kéo ")
            print("Bạn Thắng!\n Bạn có muốn chơi tiếp không!")
            win += 1
            print("Thành tích của bạn là:","\nThắng:",win,"\nHòa:",hoa,"\nThua:",loss )
            a = input("Có hoặc Không!")
            if a== "Có":
                continue
            elif a == "Không":
                break
        if comp == 2:
            print("Lựa chọn của Computer là: Búa ")
            print("Hòa!\n Bạn có muốn chơi tiếp không!")
            hoa += 1
            print("Thành tích của bạn là:","\nThắng:",win,"\nHòa:",hoa,"\nThua:",loss )
            a = input("Có hoặc Không!")
            if a== "Có":
                continue
            elif a == "Không":
                break
        if comp == 3:
            print("Lựa chọn của Computer là: Giấy ")
            loss += 1
            print("Thành tích của bạn là:","\nThắng:",win,"\nHòa:",hoa,"\nThua:",loss )
            print("Bạn thua!\n Bạn có muốn chơi tiếp không!")
            a = input("Có hoặc Không!")
            if a== "Có":
                continue
            elif a == "Không":
                break
    elif you == "Giấy":
        if comp == 1:
            print("Lựa chọn của Computer là: Kéo ")
            loss += 1
            print("Thành tích của bạn là:","\nThắng:",win,"\nHòa:",hoa,"\nThua:",loss )
            print("Bạn Thua!\n Bạn có muốn chơi tiếp không!")
            a = input("Có hoặc Không!")
            if a== "Có":
                continue
            elif a == "Không":
                break
        if comp == 2:
            print("Lựa chọn của Computer là: Búa ")
            win += 1
            print("Thành tích của bạn là:","\nThắng:",win,"\nHòa:",hoa,"\nThua:",loss )
            print("Bạn Thắng!\n Bạn có muốn chơi tiếp không!")
            a = input("Có hoặc Không!")
            if a== "Có":
                continue
            elif a == "Không":
                break
        if comp == 3:
            print("Lựa chọn của Computer là: Giấy ")
            hoa += 1
            print("Thành tích của bạn là:","\nThắng:",win,"\nHòa:",hoa,"\nThua:",loss )
            print("Hòa!\n Bạn có muốn chơi tiếp không!")
            a = input("Có hoặc Không!")
            if a== "Có":
                continue
            elif a == "Không":
                break
    else:
        break