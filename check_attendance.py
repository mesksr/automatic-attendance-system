from PyQt4 import QtGui,QtCore
import sqlite3
class CheckAttendance(QtGui.QMainWindow):
    def __init__(self):
        super(CheckAttendance, self).__init__()
        self.setGeometry(300,50,800,600)
        self.setWindowTitle("Check Attendance")
        self.setWindowIcon(QtGui.QIcon('logo1.png'))

        #Heading
        h=QtGui.QLabel(self)
        h.setAlignment(QtCore.Qt.AlignCenter)
        h.setGeometry(QtCore.QRect(250,20,300,40))
        h.setStyleSheet("QLabel { background-color : blue;color :white ; }")
        font=QtGui.QFont("Times",16,QtGui.QFont.Bold)
        h.setFont(font)
        h.setText("CHECK ATTENDANCE")

        l1=QtGui.QLabel(self)
        l1.setAlignment(QtCore.Qt.AlignCenter)
        l1.setGeometry(QtCore.QRect(40,100,80,30))
        l1.setStyleSheet("QLabel { background-color : gray;color :black ; }")
        font=QtGui.QFont("Times",13,QtGui.QFont.Bold)
        l1.setFont(font)
        l1.setText("YEAR")

        self.year=QtGui.QSpinBox(self)
        self.year.setAlignment(QtCore.Qt.AlignCenter)
        self.year.setGeometry(130,100,60,30)
        font1=QtGui.QFont("Arial",13)
        self.year.setFont(font1)
        self.year.setRange(1,4)

        l2=QtGui.QLabel(self)
        l2.setAlignment(QtCore.Qt.AlignCenter)
        l2.setGeometry(QtCore.QRect(210,100,80,30))
        l2.setStyleSheet("QLabel { background-color : gray;color :black ; }")
        l2.setFont(font)
        l2.setText("DATE")

        self.dd=QtGui.QSpinBox(self)
        self.dd.setAlignment(QtCore.Qt.AlignCenter)
        self.dd.setGeometry(300,100,50,30)
        self.dd.setFont(font1)
        self.dd.setRange(1,31)

        self.mm=QtGui.QSpinBox(self)
        self.mm.setAlignment(QtCore.Qt.AlignCenter)
        self.mm.setGeometry(350,100,50,30)
        self.mm.setFont(font1)
        self.mm.setRange(1,12)

        self.yyyy=QtGui.QSpinBox(self)
        self.yyyy.setGeometry(400,100,70,30)
        font1=QtGui.QFont("Arial",13)
        self.yyyy.setFont(font1)
        self.yyyy.setRange(2014,2050)

        l3=QtGui.QLabel(self)
        l3.setAlignment(QtCore.Qt.AlignCenter)
        l3.setGeometry(QtCore.QRect(490,100,100,30))
        l3.setStyleSheet("QLabel { background-color : gray;color :black ; }")
        l3.setFont(font)
        l3.setText("SUB CODE")
        
        self.code=QtGui.QLineEdit(self)
        self.code.setGeometry(600,100,80,30)
        self.code.setAlignment(QtCore.Qt.AlignCenter)
        self.code.setFont(font1)

        b=QtGui.QPushButton(self)
        b.setText("GO!")
        b.setFont(QtGui.QFont("Times",12,QtGui.QFont.Bold))
        b.setGeometry(700,100,60,30)
        b.setStyleSheet("QPushButton { background-color : green;color : white ; }")
        b.clicked.connect(self.show_database)

        self.text=QtGui.QPlainTextEdit(self)
        self.text.setGeometry(40,170,720,350)
        self.text.setFont(font1)

    def show_database(self):
        pass

if __name__ == '__main__':
    app = QtGui.QApplication([])
    gui = CheckAttendance()
    gui.show()
    app.exec_()
