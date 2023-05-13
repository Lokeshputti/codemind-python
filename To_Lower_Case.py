s=input()
for i in s:
    if ord(i)>=65 and ord(i)<97:
        c=ord(i)+32
        b=chr(c)
        print(b,end="")
    else:
        print(i,end="")
        