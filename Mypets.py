a= []
print("Nhập tên vật nuôi của bạn:")
b= input()
a.append(b.split(",")) # Nhập vào đã là một list rồi nên khi loại bỏ dấu "," thêm vào list mới thì nó là list con của list lớn

print("nhập tên vật nuôi muốn kiểm tra")
c = input()
if c in a[0]: 
    #
    print("Có vật nuôi "+str(c)+ "trong danh sách")
else:
    print("Không có vật nuôi "+str(c)+ " trong danh sách!")

