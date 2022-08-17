# python 3
# birthdayparadox

# 1 Số ngày sinh cần random để tính xác suất
# 2 In số ngày sinh đó ra trên màn hình( random số tháng, số ngày kết hợp với nhau)
# 3 in số ngày sinh trùng ra màn hình
# 
import time, random
import pyinputplus as pyip
print("Birthday Paradox, by Cong Binh Le lecongbinh37@gmail.com")
Month=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
print("Số ngày sinh nhật bạn muốn tính toán xác suất?(Max 100)")
# Số ngày sinh nhật muốn tính xác suất
NumBirth =pyip.inputNum()
def getMonth(NumBirth):
    getMon = []
    for i in range(NumBirth):
        random.shuffle(Month)
        num = random.randint(0,11)
        getMon.append(Month[num])
    return getMon
def getDay(NumBirth):
    day = []
    for i in range(NumBirth):
        day.append(random.randrange(1,32))
    return day
def match(getMonth, getDay, NumBirth):
    match = []
    getMon= getMonth(NumBirth)
    day = getDay(NumBirth)

    for i in range(NumBirth):
        match.append(getMon[i] + " " + str(day[i]))
        #print(match[i], end=", ")
    return match

def main(NumBirth):
    num = 0
    forn = 0 
    forMax = 100000
    print("Chương trình đang tính toán.\nVui lòng đợi trong giây lát!")
    while forn <= forMax:
        getMonth(NumBirth)
        getDay(NumBirth)
        match1 = match(getMonth, getDay, NumBirth)
        forn += 1
        for i in range(NumBirth):
            for x in range(NumBirth):
                if i != x  and match1[i] == match1[x]:
                    num += 1
                    
                else:
                    num += 0
        if forn == 10000:
            print("Đã duyệt được {}".format(forn))
        elif forn == 50000:
            print("Đã duyệt được {}. Run...".format(forn))
        elif forn == 90000:
            print("Đã duyệt được {}. \nBạn nghĩ xác suất đó là bao nhiêu!".format(forn))
        elif forn == 100000:
            print("Đã hoàn thành!")
    probability = round(num/(100000*NumBirth),2)*100
    print('Trong 100.000 lần duyệt của', NumBirth, 'người, đã phát hiện ra')
    print('số lần sinh nhật trùng khớp là', num, 'lần. Điều đó có nghĩa là')
    print('trong', NumBirth, 'người có xác suẩt', probability, '% ')
    print('có cùng ngày sinh nhật trong cùng một nhóm người.')
    print('Xác suất đó lớn hơn bạn nghĩ!')
    return probability
if __name__ == "__main__":
    main(NumBirth)


getMonth(NumBirth)
#print(getMonth(NumBirth))
#print(getDay(NumBirth))
#print(match(getMonth, getDay, NumBirth))
#print(main(NumBirth))
