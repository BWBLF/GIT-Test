import re, pyperclip, sys
#Nhấn Ctrl + A sao chếp toàn bộ text
# Nhấn Ctrl + C để copy text vào khay nhớ tạm
text= str(pyperclip.paste())
date = []
# Tạo regex phù hợp với định dạng ngày tháng năm
ngay= re.compile(r'(\d\d)(/|-|.)(\d\d)(/|-|.)(\d\d\d\d)')
xuat = ngay.findall(text)
# duyệt qua từng kết quả và lưu vào date một định dạng tiêu chuẩn
try:
    for groups in ngay.findall(text):
        if int(groups[0]) <= 31 and int(groups[2])<=12:
            if(int(groups[0]) >=30) and int(groups[2])==2:
                continue
            else:
                a="/".join([groups[0],groups[2],groups[4]])  # index nhầm, và join phải là một danh sách
                date.append(a)
        else:
            continue
    print(date)
except IndexError:
    sys.exit()

