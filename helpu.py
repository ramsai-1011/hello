def perm(x):
    if len(x)==0:
        return []
    if len(x)==1:
       # print(x)
        return [x]
    l=[]
    for i in range(len(x)):
        x1=x[i]
        xs=x[:i]+x[i+1:]
        print(xs)
        
        
        
        
        for i in perm(xs):
            #print(x1,i)
            l.append([x1]+i)
    return l
l=[1,2,3]
for i in perm(l):
    print(i)
