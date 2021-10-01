def reverse(s):
    str=""
    for i in s:
        str=i+str;
    return str

inp=input("Enter a String : ")
print("Op : "+reverse(inp))
