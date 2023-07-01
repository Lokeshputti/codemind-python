m=int(input())
if m==1 or m%3==1:
    print("HUGE")
elif m==2 or m%3==2:
    print("SMALL")
elif m==3 or m%3==0:
    print("NORMAL")