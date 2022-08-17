j =[]
c=2
def collaps(num):
    if num %2==0:
        b= num //2
        c +=2
        return b
    else :
        return (3* num +1)
a = collaps(9)
print(a)
