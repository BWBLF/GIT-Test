catsname= []
c = True
while c:
  
    print("nhập tên con mèo" + str(len(catsname)+1) + ":" +"        (Nhập khoảng trống để dừng lại!!!)" )

    a = (input())
    catsname = catsname + [a]
  
    if a == ' ' :
        c = False
print("Tên các con mèo là")
for name in catsname:
    print("   ",name)