def fibonaci(limit):
    a=0
    b=1
    print(a)
    print(b)
    for i in range(0,limit-2):
        c=a+b
        print(c)
        a=b
        b=c

inp=int(input("Enter number >"))
fibonaci(int(inp))