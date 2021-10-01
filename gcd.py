def gcd(a,b):
    if a==b:
        return a
    elif a<b:    
        for i in range(1,a+1):
            if a%i==0 and b%i==0:
                t=i
    else:
        for i in range(1,b+1):
            if a%i==0 and b%i==0:
                t=i
    return t

inp1=int(input("Enter number1 >"))
inp2=int(input("Enter number2 >"))

print(gcd(inp1,inp2))