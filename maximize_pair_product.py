'''
sum=18
a>b
a*b>'''
sum=18
m=-1
n=int(input())
a=list(map(int,input().split()))
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[i]+a[j]==sum:
            if a[i]>a[j]:
                max=a[i]*a[j]
                if max>m:
                    m=max
                    s=a[i]
                    v=a[j]
print(m,s,v)
                    






        