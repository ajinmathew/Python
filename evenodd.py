def evenodd(num):
    if num%2==0:
        return "Even"
    else:
        return "Odd"

inp=int(input("Enter a Number :"))
print("Op : "+evenodd(inp))