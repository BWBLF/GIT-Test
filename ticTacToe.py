hienthi = {"TOP_L":" ", "TOP_M":" ", "TOP_R":" ",
        "MID_L":" ", "MID_M":" ", "MID_R":" ",
        "UNDER_L":" ","UNDER_M":" ","UNDER_R":" "
        }
def choi(self):
    print(self["TOP_L"]+"|"+self["TOP_M"]+"|"+self["TOP_R"] )
    print("- + - + -")
    print(self["MID_L"]+"|"+self["MID_M"]+"|"+self["MID_R"] )
    print("- + - + -")
    print(self["UNDER_L"]+"|"+self["UNDER_M"]+"|"+self["UNDER_R"] )
player = "X"
for i in range(1,10):
    choi(hienthi)
    print("chọn ô đi tiếp theo của bạn!")
    move = input()
    hienthi[move]= player       #Đây là phép gán giá trị cho key trong từ điển  # CHƯA HIỂU  #
    if player =="X":
        player="O"
    else:
        player="X"

choi(hienthi)