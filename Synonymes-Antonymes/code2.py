from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication

def chercher():
    mot=form.mot.text()
    if (not(alpha(mot))):
        form.syno.setText("error! check your data")
        form.anto.setText("error! check your data")
    else:
        form.syno.setText(syno(mot))
        form.anto.setText(anto(mot))
def syno(mot):
    f=open("syno.txt","r")
    ch=f.readline()
    while(ch!=""):
        if(ch[0:len(mot)]==mot):
            return ch[ch.find("=")+1:len(ch)]
        ch=f.readline()
    f.close()
    return "Not Found"
def anto(mot):
    f=open("anto.txt","r")
    ch=f.readline()
    while(ch!=""):
        if(ch[0:len(mot)]==mot):
            return ch[ch.find("=")+1:len(ch)]
        ch=f.readline()
    f.close()
    return "Not Found"

def alpha(ch):
    i=0
    ch1=ch.upper()
    while(i<=len(ch1)-1):
        if not("A"<=ch1[i]<="Z"):
            return False
        i+=1
    return True


app = QApplication([])
form = loadUi("ui2.ui")
form.show()

form.chercher.clicked.connect(chercher)

app.exec_()