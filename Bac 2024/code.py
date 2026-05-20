##Evaluation.py + Consultation.py
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication,QTableWidgetItem,QMessageBox
from numpy import array
from pickle import dump, load
from random import randint
##Config
path1="Expressions.txt"
path2="Evaluations.dat"
##Les Fonctions
def generer():
    global path1
    x=randint(0,longeurtxt(path1)-1)
    f1=open(path1,"r")
    nb=0
    ch=f1.readline()
    while ch!="" and nb!=x:
        ch=ch[0:len(ch)-1]
        nb+=1
        ch=f1.readline()
    f1.close()
    form.labExp.setText(ch)
def longeurtxt(path):
    f=open(path,"r")
    nb=0
    ch=f.readline()
    while ch!="":
        nb+=1
        ch=f.readline()
    f.close()
    return nb
def valideee():
    id=form.id.text()
    rep=form.res.text()
    exp=form.labExp.text()
    if not(id.isdigit() and len(id)==8):
        QMessageBox.critical(form,"Erreur!","Verifier votre Id")
        return False
    if not(rep.isdigit() and len(rep)!=0):
        QMessageBox.critical(form,"Erreur!","Verifier votre reponse")
        return False
    if exp=="":
        QMessageBox.critical(form,"Erreur!","Generer Une Expression")
        return False
    return True
def calculer():
    global path2
    id=form.id.text()
    rep=form.res.text()
    exp=form.labExp.text()
    exp=exp[0:len(exp)-1]
    if (valideee()):
        if (int(rep)==evaluer(exp)):
            form.labRes.setText("Reponse Correct :)")
        else:
            form.labRes.setText("Reponse erronee :(")
        valide=str(int(rep)==evaluer(exp)) 
        e=dict()
        e["id"]=id
        e["exp"]=exp
        e["rep"]=rep
        e["valide"]=valide
        f=open(path2,"ab")
        dump(e,f)
        f.close()
def evaluer(ch):
    if ch.find("+") != -1:
        res = 0
        while ch.find("+") != -1:
            res += int(ch[0:ch.find("+")])
            ch = ch[ch.find("+") + 1:len(ch)]
        return res + int(ch)
    if ch.find("-") != -1:
        res = int(ch[0:ch.find("-")])
        ch = ch[ch.find("-") + 1:len(ch)]
        while ch.find("-") != -1:
            res -= int(ch[0:ch.find("-")])
            ch = ch[ch.find("-") + 1:len(ch)]
        return res - int(ch)
    if ch.find("*") != -1:
        res = 1
        while ch.find("*") != -1:
            res *= int(ch[0:ch.find("*")])
            ch = ch[ch.find("*") + 1:len(ch)]
        return res * int(ch)
    if ch.find("/") != -1:
        res = int(ch[0:ch.find("/")])
        ch = ch[ch.find("/") + 1:len(ch)]
        while ch.find("/") != -1:
            res //= int(ch[0:ch.find("/")])
            ch = ch[ch.find("/") + 1:len(ch)]
        return res // int(ch)
def afficher():
    global path2
    f=open(path2,"rb")
    test=True
    table=form.table
    table.setRowCount(0)
    table.setColumnCount(4)
    i=0
    op=form.op.currentText()
    while test:
        try:
            e=load(f)
            if(e["exp"].find(op)!=-1):
                table.insertRow(i)
                table.setItem(i,0,QTableWidgetItem(e["id"]))
                table.setItem(i,1,QTableWidgetItem(e["exp"]))
                table.setItem(i,2,QTableWidgetItem(e["rep"]))
                table.setItem(i,3,QTableWidgetItem(e["valide"]))
                i+=1
        except:
            test=False
    f.close()
##Le Programme Principale
app = QApplication([])
reponse1 = int(input("Evaluation? Consultation ==> 1 / 2 : "))
while reponse1 != 1 and reponse1 != 2:
    print("erreur!")
    reponse1 = int(input("Evaluation? Consultation ==> 1 / 2 : "))
if reponse1 == 1:  # Partie Evaluation
    form = loadUi("Interface_Evaluation.ui")
    form.show()
    form.btnExp.clicked.connect(generer)
    form.btnRes.clicked.connect(calculer)  
    form.labExp.setEnabled(False)
    app.exec_()
elif reponse1 == 2:  # Partie Consultation
    form = loadUi("Interface_Consultation.ui")
    form.show()
    form.afficher.clicked.connect(afficher)
    app.exec_()
