def puis(n,i):
    if i*i <=n:
        return i
    else:
        return puis(n,i-1)
def racine(n):
    ep=0.0000001
    t1=puis(n,n)
    t2=0.5*(t1+(n/t1))
    while abs(t1-t2)>ep:
        t1=t2
        t2=0.5*(t1+(n/t1))
    return t1
print(puis(29,29))
print(racine(29))