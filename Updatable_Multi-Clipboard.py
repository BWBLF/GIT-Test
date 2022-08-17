#Updatable Multi-Clipboard
"""
Hãy viết lại chương trình “multi-clipboard” từ Chương 6 để nó sử dụng mô -đun shelve. Bây giờ người dùng sẽ 
có thể lưu các chuỗi mới để tải vào khay nhớ tạm mà không cần phải sửa đổi mã nguồn. Chúng tôi sẽ đặt tên chương 
trình mới này là mcb.pyw (vì “mcb” ngắn hơn để nhập so với “nhiều khay nhớ tạm”). Phần mở rộng .pyw có nghĩa là Python 
sẽ không hiển thị cửa sổ Terminal khi nó chạy chương trình này. (Xem Phụ lục B để biết thêm chi tiết.)

Chương trình sẽ lưu từng đoạn văn bản clipboard dưới một từ khóa. Ví dụ: khi bạn chạy py mcb.pyw save spam , 
nội dung hiện tại của clipboard sẽ được lưu với từ khóa spam . Văn bản này sau đó có thể được tải lại vào khay nhớ tạm 
bằng cách chạy py mcb.pyw spam . Và nếu người dùng quên từ khóa họ có, họ có thể chạy danh sách py mcb.pyw để sao chép 
danh sách tất cả các từ khóa vào khay nhớ tạm.

Đây là những gì chương trình thực hiện:
    Đối số dòng lệnh cho từ khóa được kiểm tra.
    Nếu đối số được lưu , thì nội dung khay nhớ tạm được lưu vào từ khóa.
    Nếu đối số là danh sách , thì tất cả các từ khóa sẽ được sao chép vào khay nhớ tạm.
    Nếu không, văn bản cho từ khóa sẽ được sao chép vào khay nhớ tạm.
    Điều này có nghĩa là mã sẽ cần thực hiện những việc sau:

Đọc các đối số dòng lệnh từ sys.argv .
Đọc và ghi vào khay nhớ tạm.
Lưu và tải vào tệp giá sách.

CHương 9
"""
import shelve, pyperclip, sys

autoemail = shelve.open('mcb')
#Lưu nội dung vào clipboard
if len(sys.argv ) == 3 and sys.argv[1].lower() == 'save':
    autoemail[sys.argv[2]]= pyperclip.paste()
elif len(sys.argv)==2:
    # Liệt kê từ khóa và tải lại nội dung.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(autoemail.keys())))
    elif sys.argv[1] in autoemail:
        pyperclip.copy(autoemail[sys.argv[1]])


autoemail.close()