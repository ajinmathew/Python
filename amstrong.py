import math
def amstrong(num):
    temp=num
    su=0 
    while num!=0:
        s=num%10
        su=su+(s**3)
        num=num//10

    if temp==su:
        print("Amstrong")
    else:
        print("Not Amstrong")

amstrong(153)