import random
num = 1
comp = random.randint(1,20)
for i in range(6):
    b =int(input("Nhap so ban doan: "))
    print("SO BAN DOAN LA", b, ".")
    if b > comp:
        print("Số bạn đoán quá lớn .vui long doan lai.")
    elif b < comp:
        print("Số bạn đoán quá nhỏ .vui long doan lai.")
    elif b == comp:
        num = num + i
        print("Ban doan dung trong", num, "lan doan")
        break
if b!=comp:
    print ('Con số tôi đang nghĩ đến là',comp, 'lucky late.' )
