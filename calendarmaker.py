from ast import Num
import datetime
from datetime import date, time
DAY = ["Thứ 2", "Thứ 3", "Thứ 4", "Thứ 5", "Thứ 6", "Thứ Bảy", "Chủ Nhật"]
MONTH = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


#print("Hôm nay là ngày thứ ", DAY[today])
#a = datetime.day(5)
#print(a)
def Display(Month, Year):
    print(("{} - {}".format(Month, Year)).center(96, " "))
    num = 1
    daynum = 0
    day = 0
    for c in range(30):
        currentday = datetime.date(Year,Month,num)
        day = currentday.weekday()
        daynum = daynum
        num +=1
    print(day)
    print(type(day))
    if day == 0:

        pass
    for i in range(7):
        print(DAY[i].center(13, " "), end=" ")
    print()
    for i in range(6):
        rows = ['','','','','','','']
        for x in range(6):
            rows[x] = ('+-------------')*7 + "+"
            for y in range(7):
                rows[1] = ("|".ljust(14," "))
                rows[2] = ("|".ljust(14," ")) + "|"
                rows[3] = (f"|{day}".ljust(14," ")) + "|"
                rows[4] = ("|".ljust(14," ")) + "|"
                rows[5] = ("|".ljust(14," ")) + "|"
                rows[6] = ("|".ljust(14," ")) + "|"
        for row in rows:
            print(row)
    print('+-------------'*7 + "+")
def main():
    print("Calendarmaker by Le Cong Binh\n lecongbinh37@gmail.com\n\n")
    print("Nhập năm bạn muốn tìm kiếm.\nVí dụ như: 2022")
    Year = int(input("> "))
    print("Nhập tháng trong năm bạn muốn hiển thị")
    Month = int(input("> "))
    Display(Month, Year)
    #print(currentday)
        
main()
"""
import numpy as np
arr  =np.zeros(5,7)
print(arr)
"""