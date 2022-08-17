# phát hiện mật khẩu được truyền vào là mạnh
"""
Viết một hàm sử dụng biểu thức chính quy để đảm bảo rằng chuỗi mật khẩu mà nó được truyền là mạnh. 
Mật khẩu mạnh được định nghĩa là mật khẩu dài ít nhất tám ký tự, chứa cả ký tự viết hoa và viết thường và có ít nhất một chữ số. 
Bạn có thể cần phải kiểm tra chuỗi dựa trên nhiều mẫu regex để xác thực độ mạnh của nó.
"""
import re

password =input("Nhập mật khẩu của bạn:")
for i in range(0,30):
    if password[i]==" ":
        print("Nhập lại mật khẩu!")
test=[]
pas1= re.compile(r'[a-z]{8,30}')
tes1=pas1.search(password)
pas2=  re.compile(r'[A-Z]{8,30}')
tes2= pas2.search(password)
pas3=  re.compile(r'[0-9]{8,30}')
tes3= pas3.search(password)
if tes1 !="":
    if tes2!="":
        if tes2 !="":
            print("Mật khẩu truyền vào là mật khẩu mạnh!")
        else:
            print("Mật khẩu yếu!")
    else:
        print("Mật khẩu yếu!")
else:
    print("Mật khẩu yếu!")
     


               




