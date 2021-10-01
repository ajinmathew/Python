def prime(num):
    t=0
    for i in range(2,int(num/2)+1):
            if num%i==0:
                t=1
                break
    if t==0:
        return "Prime"
    else:
        return "Not Prime"

def primeRange(numL,numU):
    for i in range(numL,numU+1):
        if prime(i)=="Prime":
            print(i)
            
        
inpL=int(input("Enter a Lower Range :"))
inpU=int(input("Enter a Upper Range :"))
primeRange(inpL,inpU)