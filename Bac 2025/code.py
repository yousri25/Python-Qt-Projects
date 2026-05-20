def verif(n):
    if palindrome(n)and premier(n):
        return True
    else:
        return False
def palindrome(n):
    ch=str(n)
    ch1=""
    for i in range(len(ch)-1,-1,-1):
        ch1+=ch[i]
    return ch1==ch
def premier(n):
    for i in range(2,n//2):
        if n%i==0:
            return False
    return True
print(verif(71317))