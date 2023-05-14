x=int(input())
y=x//3600
z=(x-(y*3600))//60
p=x-((z*60)+(y*3600))
print("H:M:S-",y,":",z,":",p,sep="")