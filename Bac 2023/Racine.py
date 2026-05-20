from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication,QTableWidgetItem
from numpy import array
from pickle import dump, load
##Config
path="Approchee.dat"
##Les Fonctions
def ajouter():
    global path
    f=open(path,"ab")
    x=int(form.xx.text())
    e=dict()
    e["x"]=x
    e["RC"]=racine(x)
    dump(e,f)
    f.close()
def afficher():
    global path
    f = open(path,"rb")
    i = 0
    form.table.setRowCount(0)
    form.table.setColumnCount(2)
    test=True
    while test==True:
        try:
            e = load(f)
            form.table.insertRow(i)
            form.table.setItem(i, 0, QTableWidgetItem(str(e["x"])))
            form.table.setItem(i, 1, QTableWidgetItem(str(e["RC"])))
            i += 1
        except:
            test=False
    f.close()
def longeur(path):
    f=open(path,"rb")
    test=True
    nb=0
    while test:
        try:
            e=load(f)
            nb+=1
        except:
            test=False
    f.close()
    return nb
def racine(n):
    ep=0.0000001
    t1=puis(n,n)
    t2=0.5*(t1+(n/t1))
    while abs(t1-t2)>ep:
        t1=t2
        t2=0.5*(t1+(n/t1))
    return t1
def puis(n,i):
    if i*i <=n:
        return i
    else:
        return puis(n,i-1)
##Le Programme Principale
app = QApplication([])
form = loadUi("Interface_Racine.ui")
form.show()

form.ajouter.clicked.connect(ajouter)
form.afficher.clicked.connect(afficher)

app.exec_()