import pyinputplus as pyip
while True:
    print("Bạn muốn khiến một kẻ ngốc bận rộn hàng giờ không!")
    text= pyip.inputYesNo()
    if text =='no':
        print("Chương trình kết thúc!")
        break
    if text =="yes":
        pass

print("Chúc bạn một ngày tốt lành!")

from pathlib import Path
import os
Path.cwd()