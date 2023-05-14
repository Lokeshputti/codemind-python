p=int(input())
r=int(input())
t=int(input())
a=p*((1+r/100)**t)
ci=a-p
print("{:.2f}".format(ci))