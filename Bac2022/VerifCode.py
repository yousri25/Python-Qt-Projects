##Config
path="Codes.txt"
##Les Fonctions
def VerifCode(ch):
    global path
    if(verif(ch)):
        test=False
        f=open(path,"r")
        ch1=f.readline()
        while(ch1!=""):
            ch1=ch1[0:len(ch1)-1]
            if(ch1==ch):
                test=True
            ch1=f.readline()
        if(test):
            print("Code Valide")
        else:
            print("Code deja utilise")
    else:
        print("Code non valide")
def verif(ch):
    if(len(ch)!=13):
        return False
    n1=int(ch[0:3])
    n2=int(ch[3:8])
    n3=int(ch[8:13])
    if not(premier(n1)):
        return False
    if not(verifbin(n2)):
        return False
    if not(n3 % n1 ==0):
        return False
    return True
def premier(n):
    if n==1:
        return True
    else:
        for i in range(2,n//2 +1):
            if n % i ==0:
                return False
    return True
def verifbin(n):
    x=binaire(n)
    nb=0
    for i in range(len(x)):
        if x[i]=="0":
            nb+=1
    return nb>8
def binaire(n):
    if n==0:
        return "0"
    else:
        return binaire(n//2)+str(n%2)
##Le Programme Principale
ch=input("Donner Votre Code De Recharge")
VerifCode(ch)