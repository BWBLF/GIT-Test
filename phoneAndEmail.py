#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip, re
# Create Phone regex. (000-000-0000)or (000)-000-000 or 000.000.0000 or 000 000 0000
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    )''', re.VERBOSE)



# Create email regex. asdjk87!@#$%^&*(6879@gmail.com
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+      # username
    @                      # @ symbol
    [a-zA-Z0-9.-]+         # domain name
    (\.[a-zA-Z]{2,4})       # dot-something
    )''', re.VERBOSE)



# Find matches in clipboard text.
text = str(pyperclip.paste())
matches = []

for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])


# Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')



"""
Ý tưởng cho các chương trình tương tự

Việc xác định các mẫu văn bản (và có thể thay thế chúng 
bằng phương thức sub () ) có nhiều ứng dụng tiềm năng khác nhau. Ví dụ, bạn có thể:
Tìm URL của trang web bắt đầu bằng http: // hoặc https: // .
Dọn dẹp các ngày ở các định dạng ngày khác nhau (chẳng hạn như 14/3/2019, 14/3/2019 
và 2015/3/19) bằng cách thay thế chúng bằng các ngày ở một định dạng chuẩn, duy nhất.
Xóa thông tin nhạy cảm như số An sinh xã hội hoặc số thẻ tín dụng.
Tìm các lỗi chính tả phổ biến như nhiều khoảng trắng giữa các từ, các từ được lặp lại
 một cách vô tình hoặc nhiều dấu chấm than ở cuối câu. Thật là khó chịu !!
"""