inventory= {'wire': 1, 'torch': 6, 'gold coins': 42, 'dagger': 1, 'arrow': 12}
def displayinventory(inven):
    print("Hàng tồn kho:".center(30,"-"))
    for k,v in inventory.items():
        print(k.ljust(15,".")+str(v).rjust(5," "))
print('\n\n\n')
dragonloop=['gold coins', 'dagger', 'gold coins', 'gold coins', 'ruby']
def invento(nhat):
    global j
    j ={}
    for i in nhat:
        j.setdefault(i,1)
        j[i]=j[i]+1
    for k in inventory.keys():
        for a in j.keys():
            if k ==a:
                inventory[k]=inventory[k]+1
            else:
                inventory.setdefault(a,1)
    for k,v in inventory.items():
            print(k.ljust(15,".")+str(v).rjust(5," "))

displayinventory(inventory)
invento(dragonloop)












