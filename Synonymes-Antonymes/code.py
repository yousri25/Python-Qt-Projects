from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
def fermer():
    form.close()
def effacer():
    form.res.setText("")
    form.mot.setText("")
    form.syn.setText("")
    form.ant.setText("")

def ajout():
    a=form.mot.text()
    b=form.syn.text()
    c=form.ant.text()
    if not(alpha(a) and alpha(b) and alpha(c)):
        form.res.setText("Verifier Votre Donnees")
    else:
        f1=open("mot.txt","a")
        f2=open("syno.txt","a")
        f3=open("anto.txt","a")
        f1.write(a)
        f2.write(a+"="+b)
        f3.write(a+"="+c)
        f1.close()
        f2.close()
        f3.close()
        form.res.setText("Ajout Terminer")
def alpha(ch):
    ch1=ch.upper()
    i=0
    while (i<=len(ch)-1):
        if not("A"<=ch1[i]<="Z"):
            return False
        i+=1
    return True
    
def open_dic():
    app = QApplication([])
    form2 = loadUi("ui2.ui")
    form2.show()
    app.exec_()

app = QApplication([])
form = loadUi("ui.ui")
form.show()

form.ajout.clicked.connect(ajout)
form.eff.clicked.connect(effacer)
form.fer.clicked.connect(fermer)
form.dic.clicked.connect(open_dic)

app.exec_()

