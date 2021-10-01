def prime(num):
    if num > 2:
        for i in range(2,int(num/2)+1):
            if num%i==0:
                return "Not Prime"
                break
        return "Prime"
        
inp=int(input("Enter a Number :"))
print("Op : "+prime(inp))