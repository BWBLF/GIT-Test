allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}
def tinhtong(khachhang,vatpham):
    num = 0
    for k, v in khachhang.items():
        num = num  + v.get(vatpham,0)
    return num
print("- Táo        :" + str(tinhtong(allGuests,'apples')) )
print("- Cups       :" + str(tinhtong(allGuests,'cups')) )
print("- Sanwichs   :" + str(tinhtong(allGuests,'ham sandwiches')) )
print("- Pies       :" + str(tinhtong(allGuests,'apple pies')) )
print("- pretzels   :" + str(tinhtong(allGuests,'pretzels')) )
