import pyinputplus as pyip
import pandas as pd
f = open("sinhvien.txt", "a+", encoding="utf-8")
num = 0 
while True:
    MaSV = input("Nhập mã SV(Không nhập gì để thoát): ")
    if MaSV=="":
        break
    else:
        Ten = input("Nhập tên sinh viên: ")
        num = num + 1
        email = pyip.inputEmail("Nhập email: ")
        Andress = input("Nhập địa chỉ: ")
        Phone = input("Nhập số điện thoại: ")
        Gtinh = input("Nhập giới tính: ")
        f.write("\t".join([MaSV, Ten, email, Andress, Phone, Gtinh]) + "\n") 
print("cách 2:")
a = "sinhvien.txt"
SV = pd.read_csv (a, sep="\t", names=["Mã SV", " Tên SV", "Email", "Địa Chỉ", "Điện thoại", "Giới tính"])
print(SV)
# sắp xếp dữ liệu
DSSV = SV.sort_values("Giới tính")
# lọc dữ liệu theo từng trường
Loc = SV.query('Tên SV=="Dương"')
print(DSSV)
print(Loc)
f.close()