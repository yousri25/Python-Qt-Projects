from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication , QMessageBox , QTableWidgetItem
from numpy import array
from pickle import dump, load

path1="terme.txt"
path2="suites.dat"

def sauvgarder_txt():
    global path1
    n=form.nn.text()
    if not(n.isdecimal()):
        QMessageBox.critical(form,"Erreur!","donnee n'est pas numerique")
    else:
        if not(1<=int(n)<=50):
            QMessageBox.critical(form,"Erreur!","N doit verifier : 1<=N<=50")
        else:
            if(existe(n,path1)):
                QMessageBox.warning(form,"Warning","N deja existe dans terme.txt")
            else:
                f=open(path1,"a")
                f.write(n+"\n")
                f.close()
                QMessageBox.information(form,"Success","N sauvgardee avec succes.")

def existe(n,path):
    f=open(path,"r")
    ch=f.readline()
    while(ch!=""):
        if(ch[0:len(ch)-1]==n):
            f.close()
            return True
        ch=f.readline()
    f.close()
    return False

def cree():
    global path2
    f=open(path2,"wb")
    f.close()
    QMessageBox.information(form,"Success","Suites.dat a ete cree avec succes")

def affichier():
    global path1,path2
    if(form.s1.isChecked()==False and form.s2.isChecked()==False):
        QMessageBox.critical(form,"Error!","Veillez choisir une Suite (S1 ou S2)")
    else:
        if(form.liste.currentIndex()==0):
            QMessageBox.warning(form,"Warning","Veuillez choisir le mode d'affichage")
        else:
            f=open(path2,"wb")
            f.close()

            if(form.s1.isChecked()):
                if(form.liste.currentIndex()==1):
                    suite1nieme(path1,path2)
                    afficher2(path2)
                else:
                    suite1tousterme(path1,path2)
                    afficher2(path2)
            elif(form.s2.isChecked()):
                if(form.liste.currentIndex()==1):
                    suite2nieme(path1,path2)
                    afficher2(path2)
                else:
                    suite2tousterme(path1,path2)
                    afficher2(path2)

def afficher2(path2):
    form.table.setRowCount(longeur(path2)+1)
    form.table.setColumnCount(3)
    form.table.setItem(0,0,QTableWidgetItem("Rang"))
    form.table.setItem(0,1,QTableWidgetItem("Valeur"))
    form.table.setItem(0,2,QTableWidgetItem("Type"))
    test=True
    i=1
    f=open(path2,"rb")
    while test:
        try:
            e=load(f)
            form.table.setItem(i,0,QTableWidgetItem(str(e["rang"])))
            form.table.setItem(i,1,QTableWidgetItem(str(e["valeur"])))
            form.table.setItem(i,2,QTableWidgetItem(str(e["type"])))
            i+=1
        except:
            test=False
    f.close()

def longeur(path2):
    test=True
    nb=0
    try:
        f=open(path2,"rb")
        while test:
            try:
                load(f)
                nb+=1
            except:
                test=False
        f.close()
    except:
        pass
    return nb

def suite2tousterme(path1,path2):
    f=open(path1,"r")
    n=f.readline()
    while(n!=""):
        calc2(n[0:len(n)-1],path2)
        n=f.readline()
    f.close()

def calc2(n,path2):
    for i in range(1,int(n)+1):
        e={
                "rang":str(i),
                "valeur":str(calculns2(i)),
                "type":"Suite 2"
            }
        f=open(path2,"ab")
        dump(e,f)
        f.close()

def suite1tousterme(path1,path2):
    f=open(path1,"r")
    n=f.readline()
    while(n!=""):
        calc1(n[0:len(n)-1],path2)
        n=f.readline()
    f.close()

def calc1(n,path2):
    for i in range(1,int(n)+1):
        e={
                "rang":str(i),
                "valeur":str(calculns1(i)),
                "type":"Suite 1"
            }
        f=open(path2,"ab")
        dump(e,f)
        f.close()

def suite1nieme(path1,path2):
    f=open(path1,"r")
    n=f.readline()
    while(n!=""):
        n=n[0:len(n)-1]
        e={
                "rang":n,
                "valeur":str(calculns1(int(n))),
                "type":"Suite 1"
            }
        f2=open(path2,"ab")
        dump(e,f2)
        f2.close()
        n=f.readline()
    f.close()

def suite2nieme(path1,path2):
    f=open(path1,"r")
    n=f.readline()
    while(n!=""):
        n=n[0:len(n)-1]
        e={
                "rang":n,
                "valeur":str(calculns2(int(n))),
                "type":"Suite 2"
            }
        f2=open(path2,"ab")
        dump(e,f2)
        f2.close()
        n=f.readline()
    f.close()

def calculns1(n):
    if(n<=1):
        return 2
    else:
        return 2*calculns1(n-1)+1

def calculns2(n):
    if (n<=1):
        return 1
    else:
        return calculns2(n-1)+calculns2(n-2)

app = QApplication([])
form = loadUi("ui.ui")
form.show()

form.sauv.clicked.connect(sauvgarder_txt)
form.cree.clicked.connect(cree)
form.afficher.clicked.connect(affichier)

app.exec_()
