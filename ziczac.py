import time, sys
thutlekhong = True
thutle = 0
try:
    while True:
        print(' ' * thutle, end=' ')
        print("********")
        time.sleep(0.05) 
        
        if thutlekhong:
            thutle += 1
            if thutle ==20:
                thutlekhong = False
        else:
            thutle -= 1
            if thutle ==0:
                thutlekhong = True
                #continue  có cũng được vì while luôn đúng
except KeyboardInterrupt:
    sys.exit()



