s1=input()
s2=input()
c=s2[len(s2)-1]
l=list(s1)
l.sort()
if(c in l):
    a=l.index(c)
    r=0
    while(l[a]==c):
        r=r+1
        a=a+1
    print(r)
else:
    print(0)
