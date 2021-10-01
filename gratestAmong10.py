# gratest among 10 numbers
li=[]
for i in range(0,10):
    l=int(input("Enter number >"))
    li.append(l)
li.sort()
print(li[-1])