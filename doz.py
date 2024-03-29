
from PyQt6 import QtCore, QtGui, QtWidgets 
from PyQt6.QtWidgets import*
from PyQt6.QtCore import*
from PyQt6.QtGui import*




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("doz")
        MainWindow.resize(419, 439)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -100, 611, 571))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Wallpaper Gif Full HD - Rhenan Lourenço ®.jpg"))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 111, 121))
        self.pushButton.setStyleSheet("background-color: rgb(170, 0, 255);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.input_text)
        self.pushButton.clicked.connect(self.input_text_o)
        self.pushButton.clicked.connect(self.button)
        self.pushButton.clicked.connect(self.button_o)


        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 0, 111, 121))
        self.pushButton_2.setStyleSheet("background-color: rgb(170, 0, 255);")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.input_text)
        self.pushButton_2.clicked.connect(self.button)
        self.pushButton_2.clicked.connect(self.button_o)
        self.pushButton_2.clicked.connect(self.input_text_o)



        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(290, 0, 111, 121))
        self.pushButton_3.setStyleSheet("background-color: rgb(170, 0, 255);")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.input_text)
        self.pushButton_3.clicked.connect(self.button)
        self.pushButton_3.clicked.connect(self.input_text_o)
        self.pushButton_3.clicked.connect(self.button_o)


        self.pushButton_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 130, 111, 121))
        self.pushButton_4.setStyleSheet("background-color: rgb(170, 0, 255);")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.input_text)
        self.pushButton_4.clicked.connect(self.button)
        self.pushButton_4.clicked.connect(self.input_text_o)
        self.pushButton_4.clicked.connect(self.button_o)


        self.pushButton_5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(150, 130, 111, 121))
        self.pushButton_5.setStyleSheet("background-color: rgb(170, 0, 255);")
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.input_text)
        self.pushButton_5.clicked.connect(self.button)
        self.pushButton_5.clicked.connect(self.input_text_o)
        self.pushButton_5.clicked.connect(self.button_o)


        self.pushButton_6 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(290, 130, 111, 121))
        self.pushButton_6.setStyleSheet("background-color: rgb(170, 0, 255);")
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.input_text)
        self.pushButton_6.clicked.connect(self.button)
        self.pushButton_6.clicked.connect(self.input_text_o)
        self.pushButton_6.clicked.connect(self.button_o)


        self.pushButton_7 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(290, 270, 111, 121))
        self.pushButton_7.setStyleSheet("background-color: rgb(170, 0, 255);")
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.input_text)
        self.pushButton_7.clicked.connect(self.button)
        self.pushButton_7.clicked.connect(self.input_text_o)
        self.pushButton_7.clicked.connect(self.button_o)


        self.pushButton_8 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(150, 270, 111, 121))
        self.pushButton_8.setStyleSheet("background-color: rgb(170, 0, 255);")
        self.pushButton_8.setText("")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(self.input_text)
        self.pushButton_8.clicked.connect(self.button)
        self.pushButton_8.clicked.connect(self.input_text_o)
        self.pushButton_8.clicked.connect(self.button_o)


        self.pushButton_9 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(0, 260, 111, 121))
        self.pushButton_9.setStyleSheet("background-color: rgb(170, 0, 255);")
        self.pushButton_9.setText("")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.clicked.connect(self.input_text)
        self.pushButton_9.clicked.connect(self.button)
        self.pushButton_9.clicked.connect(self.input_text_o)
        self.pushButton_9.clicked.connect(self.button_o)


        self.pushButton_10 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(30, 390, 111, 30))
        self.pushButton_10.setStyleSheet("background-color: rgb(191 , 0 , 255)")
        self.pushButton_10.setText("Clean")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.setFont(QFont("Arial" , 12))
        self.pushButton_10.clicked.connect(self.button_clean)


        self.text = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.text.setStyleSheet("background-color: rgb(0, 21, 255);")
        self.text.setGeometry(300, 390, 111, 30)
        self.text.setObjectName("QLineEdit")


        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setText("Enter x or o :")
        self.label.setFont(QFont("Arial" , 10))
        self.label.setStyleSheet("background-color: rgb(0, 21, 255);")
        self.label.setGeometry(220, 390, 80, 30)  # Adjust the width and height as needed
        self.label.setObjectName("QLabel")


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 419, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "doz"))
    
    
    def input_text(self):
        if self.text.text()=="x":
            self.pushButton.clicked.connect(lambda:self.pushButton.setText("x"))
            self.pushButton_2.clicked.connect(lambda:self.pushButton_2.setText("x"))
            self.pushButton_3.clicked.connect(lambda:self.pushButton_3.setText("x"))
            self.pushButton_4.clicked.connect(lambda:self.pushButton_4.setText("x"))
            self.pushButton_5.clicked.connect(lambda:self.pushButton_5.setText("x"))
            self.pushButton_6.clicked.connect(lambda:self.pushButton_6.setText("x"))
            self.pushButton_7.clicked.connect(lambda:self.pushButton_7.setText("x"))
            self.pushButton_8.clicked.connect(lambda:self.pushButton_8.setText("x"))
            self.pushButton_9.clicked.connect(lambda:self.pushButton_9.setText("x"))

    def input_text_o(self):
        if self.text.text()=="o":
            self.pushButton.clicked.connect(lambda:self.pushButton.setText("o"))
            self.pushButton_2.clicked.connect(lambda:self.pushButton_2.setText("o"))
            self.pushButton_3.clicked.connect(lambda:self.pushButton_3.setText("o"))
            self.pushButton_4.clicked.connect(lambda:self.pushButton_4.setText("o"))
            self.pushButton_5.clicked.connect(lambda:self.pushButton_5.setText("o"))
            self.pushButton_6.clicked.connect(lambda:self.pushButton_6.setText("o"))
            self.pushButton_7.clicked.connect(lambda:self.pushButton_7.setText("o"))
            self.pushButton_8.clicked.connect(lambda:self.pushButton_8.setText("o"))
            self.pushButton_9.clicked.connect(lambda:self.pushButton_9.setText("o"))
              
    def button(self):
        if self.pushButton.text()=="x" and self.pushButton_5.text()=="x" and self.pushButton_7.text()=="x":
            messgae=QMessageBox()
            messgae.setText("X is winer")
            messgae.exec()

        elif self.pushButton.text() =="x" and self.pushButton_2.text()=="x" and self.pushButton_3.text()=="x":
            messgae=QMessageBox()
            messgae.setText("X is winer")
            messgae.exec()

        elif self.pushButton_4.text() =="x" and self.pushButton_5.text()=="x" and self.pushButton_6.text()=="x":
            messgae=QMessageBox()
            messgae.setText("X is winer")
            messgae.exec()

        elif self.pushButton_7.text() =="x" and self.pushButton_8.text()=="x" and self.pushButton_9.text()=="x":
            messgae=QMessageBox()
            messgae.setText("X is winer")
            messgae.exec()

        elif self.pushButton_3.text() =="x" and self.pushButton_5.text()=="x" and self.pushButton_9.text()=="x":
            messgae=QMessageBox()
            messgae.setText("X is winer")
            messgae.exec()
        
    def button_o(self):
        if self.pushButton.text()=="o" and self.pushButton_5.text()=="o" and self.pushButton_7.text()=="o":
            messgae=QMessageBox()
            messgae.setText("O is winer")
            messgae.exec()
        elif self.pushButton.text() =="o" and self.pushButton_2.text()=="o" and self.pushButton_3.text()=="o":
            messgae=QMessageBox()
            messgae.setText("O is winer")
            messgae.exec()

        elif self.pushButton_4.text() =="o" and self.pushButton_5.text()=="o" and self.pushButton_6.text()=="o":
            messgae=QMessageBox()
            messgae.setText("X is winer")
            messgae.exec()

        elif self.pushButton_7.text() =="o" and self.pushButton_8.text()=="o" and self.pushButton_9.text()=="o":
            messgae=QMessageBox()
            messgae.setText("o is winer")
            messgae.exec()

        elif self.pushButton_3.text() =="o" and self.pushButton_5.text()=="o" and self.pushButton_9.text()=="o":
            messgae=QMessageBox()
            messgae.setText("o is winer")
            messgae.exec()
            self.text.setText("")
        

    def button_clean(self):
        self.text.setText("")
        self.pushButton.setText("")
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.pushButton_4.setText("")
        self.pushButton_5.setText("")
        self.pushButton_6.setText("")
        self.pushButton_7.setText("")
        self.pushButton_8.setText("")
        self.pushButton_9.setText("")

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())