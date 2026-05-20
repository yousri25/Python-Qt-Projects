from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from pickle import load,dump
from numpy import array
##Config
path1="Quiz.dat"
path2="Reponses.dat"
##Les Fonctions
def test():
    ##Module Principale
    global path1
    id=form.id.text()
    if not verifid(id):
        QMessageBox.critical(form,"Erreur","L'identifiant doit commencer par 2 lettres suivies par 6 chiffres")
    elif exist(id):
        QMessageBox.critical(form,"Erreur","Vous avez dejà participé au quiz!")
    else:
        nb=0##L'indice de Tquiz Commence par 0
        f=open(path1,"rb")
        e=load(f)
        form.labNum.setText(str(nb))
        form.labQues.setText(e["ques"])
        form.labP1.setText(e["p1"])               
        form.labP2.setText(e["p2"])
        f.close()##Fermeture de Fichier
def afficher():
    ##Module test pour afficher le contenue de fichier Quiz.dat
    global path1
    f=open(path1,"rb")
    test=True
    while test:
        try:
            e=load(f)
            print(e)
        except:
            test=False
    f.close()
def verifid(id):
    #permet de contrôler la validité de l’identifiant id saisi
    if len(id)!=8:
        return False
    id=id.upper()
    if not("A"<=id[0]<="Z" and "A"<=id[1]<="Z"):
        return False
    for i in range(2,len(id)):
        if not("0"<=id[i]<="9"):
            return False
    return True
def exist(id):
    #permet de vérifier l’existence de l’identifiant id dans le fichier "Reponses.dat"
    global path2
    test=True
    f=open(path2,"rb")
    while test:
        try:
           e=load(f)
           if e["id"]==id:
            f.close()
            return True 
        except:
            test=False
    f.close()
    return False
def remplirQuiz(n,Tquiz):
    #permet de transférer le contenu du fichier "Quiz.dat" vers le tableau Tquiz
    global path1
    f=open(path1,"rb")
    test=True
    i=0
    while test:
        try:
            e=load(f)
            Tquiz[i]=e
            i+=1     
        except:
            test=False
    f.close()
def afficherQuestion(num,Tquiz):
    #permet d’afficher à partir du tableau Tquiz, les données relatives à la question numéro num.
    form.labNum.setText(str(num))
    form.labQues.setText(str(Tquiz[num]["ques"]))
    form.labP1.setText(str(Tquiz[num]["p1"]))
    form.labP2.setText(str(Tquiz[num]["p2"]))
def validation():
    ##Valider La Reponse et Continuer/Terminer le test
    global path2,n,Tquiz,Trep,nbq
    id=form.id.text()
    if nbq<n-1:
        ques=form.labQues.text()
        if form.rd1.isChecked():
            nump=1
        elif form.rd2.isChecked():
            nump=2
        else:
            QMessageBox.critical(form,"Erreur","Choisissez une réponse")
        Trep[nbq]=dict()
        Trep[nbq]["id"]=id
        Trep[nbq]["ques"]=ques
        Trep[nbq]["nump"]=nump
        afficherQuestion(nbq+1,Tquiz)
        nbq+=1
    else:
        f=open(path2,"ab")
        for i in range(n):
            dump(Trep[i],f)
        f.close()
        QMessageBox.information(form,"Fin Test","Fin Test")
        form.labRes.setText("Tu as "+str(correct(Tquiz,Trep,n))+" Reponse(s) Correcte(s) de "+str(n)+" Questions")
def correct(Tquiz,Trep,n):
    nb=0
    for i in range(n):
        if Trep[i]["nump"]==Tquiz[i]["rep"] :
            nb+=1
    return nb
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
##Le Programme Principale
print("Code done by Yousri :)")
nbq=0## L'indice de question actuelle
n=longeur(path1) ##Longeur de fichier Quiz.dat
Tquiz=array([dict()]*n)##Tableau Des Question
Trep=array([dict()]*n)##Tableau Des Reponses
remplirQuiz(n,Tquiz)##Remplir le Tableau (Un seul Appel)
app = QApplication([])
form = loadUi ("Interface_Reponse.ui")
form.show()
form.blancer.clicked.connect (test)
form.bvalider.clicked.connect (validation)
app.exec_()