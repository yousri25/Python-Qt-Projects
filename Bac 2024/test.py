from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication,QTableWidgetItem,QMessageBox
from numpy import array
from pickle import dump, load
from random import randint
path="Evaluations.dat"
def afficher(path):
    f=open(path,"rb")
    test=True
    while test:
        try:
            e=load(f)
            print(e)
        except:
            test=False
    f.close()
afficher(path)
