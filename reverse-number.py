def reverse(num):
    temp=0
    while num>0:
        n=num%10
        temp=temp*10+n
        num=num//10
    return temp

inp=int(input("Enter a String :"))
print(reverse(inp))