def fact(num):
    if num>1:
        num=num*fact(num-1)
    return num
inp=int(input("Enter a Number :"))
print(fact(inp))