#-------------------------------------------------------------------------------
# Name:        calculadora-pyqt5
# Purpose:     simple calculator written in python and pyqt5
#
# Author:      Armando
#
# Created:     23/07/2018
# Copyright:   (c) ARMANDO 2018
#
#-------------------------------------------------------------------------------
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow,QPushButton, QDesktopWidget
from PyQt5 import uic

class Ventana(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("calculadora.ui",self)
        self.resize(400,250)
        #hay que fijar el tamaño
        self.Center()
        self.uno.clicked.connect(self.presUno)
        self.dos.clicked.connect(self.presDos)
        self.tres.clicked.connect(self.presTres)
        self.cuatro.clicked.connect(self.presCuatro)
        self.cinco.clicked.connect(self.presCinco)
        self.seis.clicked.connect(self.presSeis)
        self.siete.clicked.connect(self.presSiete)
        self.ocho.clicked.connect(self.presOcho)
        self.nueve.clicked.connect(self.presNueve)
        self.cero.clicked.connect(self.presCero)
        self.suma.clicked.connect(self.presSuma)
        self.resta.clicked.connect(self.presResta)
        self.multiplicacion.clicked.connect(self.presMultiplicacion)
        self.division.clicked.connect(self.presDivision)
        self.igual.clicked.connect(self.presIgual)
        self.limpiar.clicked.connect(self.presLimpiar)
        self.b=0#bandera de control


    def Center(self):
        qr=self.frameGeometry()
        cp=QDesktopWidget().availableGeometry().center()


    def presUno(self):

        #tomo el texto de la pantalla
        if self.b==1:
            self.pantalla.setText("")
        else:
            pass
        campo=self.pantalla.text()
        numero=self.uno.text()#tomo el texto del boton
        self.pantalla.setText(campo+numero)#concateno el texto y lo inserto
        self.b=0
        print(self.b)


    def presDos(self):
        if self.b==1:
            self.pantalla.setText("")
        else:
            pass
        campo=self.pantalla.text()
        numero=self.dos.text()
        self.pantalla.setText(campo+numero)
        self.b=0
        print(self.b)


    def presTres(self):
        if self.b==1:
            self.pantalla.setText("")
        else:
            pass
        campo=self.pantalla.text()
        numero=self.tres.text()
        self.pantalla.setText(campo+numero)
        self.b=0

    def presCuatro(self):
        if self.b==1:
            self.pantalla.setText("")
        else:
            pass
        campo=self.pantalla.text()
        numero=self.cuatro.text()
        self.pantalla.setText(campo+numero)
        self.b=0

    def presCinco(self):
        if self.b==1:
            self.pantalla.setText("")
        else:
            pass

        campo=self.pantalla.text()
        numero=self.cinco.text()
        self.pantalla.setText(campo+numero)
        self.b=0

    def presSeis(self):
        if self.b==1:
            self.pantalla.setText("")
        else:
            pass
        campo=self.pantalla.text()
        numero=self.seis.text()
        self.pantalla.setText(campo+numero)
        self.b=0

    def presSiete(self):
        if self.b==1:
            self.pantalla.setText("")
        else:
            pass
        campo=self.pantalla.text()
        numero=self.siete.text()
        self.pantalla.setText(campo+numero)
        self.b=0

    def presOcho(self):
        if self.b==1:
            self.pantalla.setText("")
        else:
            pass
        campo=self.pantalla.text()
        numero=self.ocho.text()
        self.pantalla.setText(campo+numero)
        self.b=0

    def presNueve(self):
        if self.b==1:
            self.pantalla.setText("")
        else:
            pass
        campo=self.pantalla.text()
        numero=self.nueve.text()
        self.pantalla.setText(campo+numero)
        self.b=0

    def presCero(self):
        if self.b==1:
            self.pantalla.setText("")
        else:
            pass
        campo=self.pantalla.text()
        numero=self.cero.text()
        self.pantalla.setText(campo+numero)
        self.b=0

    def presSuma(self):
        campo=self.pantalla.text()
        numero=self.suma.text()
        self.pantalla.setText(campo+numero)

    def presResta(self):
        campo=self.pantalla.text()
        numero=self.resta.text()
        self.pantalla.setText(campo+numero)

    def presMultiplicacion(self):
        campo=self.pantalla.text()
        numero=self.multiplicacion.text()
        self.pantalla.setText(campo+numero)

    def presDivision(self):
        campo=self.pantalla.text()
        numero=self.division.text()
        self.pantalla.setText(campo+numero)

    def presIgual(self):


        campo=self.pantalla.text()#tomo el texto de la pantalla
        try:
            resultado=eval(campo)
            self.pantalla.setText(str(resultado))



        except:
            self.pantalla.setText("Error, Sintaxis Incorrecta")
        self.b=1

    def presLimpiar(self):
        campo=self.pantalla.text()
        if campo!=[]:
            self.pantalla.setText("")
            self.b=0




#instancia para la aplicacion

app=QApplication(sys.argv)

ventana=Ventana()

ventana.show()
app.exec_()


