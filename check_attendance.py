from PyQt4 import QtGui,QtCore
import sqlite3
import datetime


conn=sqlite3.connect('Attendance System.db')
c=conn.cursor()
 
class CheckAttendance(QtGui.QMainWindow):
    def __init__(self,sub):
        self.subject=sub
        
        super(CheckAttendance, self).__init__()
        self.setGeometry(300,50,800,600)
        self.setWindowTitle("Check Attendance")
        self.setWindowIcon(QtGui.QIcon('other_images/logo.png'))

        #Heading
        h=QtGui.QLabel(self)
        h.setAlignment(QtCore.Qt.AlignCenter)
        h.setGeometry(QtCore.QRect(250,20,300,40))
        h.setStyleSheet("QLabel { background-color : blue;color :white ; }")
        font=QtGui.QFont("Times",16,QtGui.QFont.Bold)
        h.setFont(font)
        h.setText("CHECK ATTENDANCE")

        #Label and Date Entry Spinbox
        l2=QtGui.QLabel(self)
        l2.setAlignment(QtCore.Qt.AlignCenter)
        l2.setGeometry(QtCore.QRect(230,100,80,30))
        l2.setStyleSheet("QLabel { background-color : gray;color :black ; }")
        font1=QtGui.QFont("Times",14,QtGui.QFont.Bold)
        l2.setFont(font1)
        l2.setText("DATE")

        self.dd=QtGui.QSpinBox(self)
        self.dd.setAlignment(QtCore.Qt.AlignCenter)
        self.dd.setGeometry(330,100,50,30)
        self.dd.setFont(font1)
        self.dd.setRange(1,31)
        self.dd.setValue(datetime.date.today().day)

        self.mm=QtGui.QSpinBox(self)
        self.mm.setAlignment(QtCore.Qt.AlignCenter)
        self.mm.setGeometry(380,100,50,30)
        self.mm.setFont(font1)
        self.mm.setRange(1,12)
        self.mm.setValue(datetime.date.today().month)

        self.yyyy=QtGui.QSpinBox(self)
        self.yyyy.setGeometry(430,100,70,30)
        self.yyyy.setFont(font1)
        self.yyyy.setRange(2014,2050)
        self.yyyy.setValue(datetime.date.today().year)

        #Go Button to check specific Date's Attendance
        b=QtGui.QPushButton(self)
        b.setText("GO!")
        b.setFont(font1)
        b.setGeometry(510,100,60,30)
        b.setStyleSheet("QPushButton { background-color : green;color : white ; }")
        b.clicked.connect(self.show_database)
        
        #Text Area To display database
        self.text=QtGui.QTextEdit(self)
        self.text.setGeometry(40,170,720,350)
        self.text.setFont(font1)

        #Default Display of Subject's Total Attendance on every date
        xyear = (int(self.subject[2])+1)//2
        query='SELECT * FROM YEAR{}'.format(xyear)
        c.execute(query)
        rolls = []
        names = []
        for row in c.fetchall():
            rolls.append(row[0])
            names.append(row[1])
            
        self.text.insertPlainText('Roll\tName\tAttendance %\n')
                
        for i in range(len(rolls)):
            query='SELECT ['+ str(rolls[i]) + '] FROM {}'.format(self.subject)
            print (query)
            c.execute(query)
            p = 0 #present
            a = 0 #absent
            for row in c.fetchall():
                if (row[0] == 'P'):
                    p += 1
                else:
                    a += 1
            self.text.insertPlainText(str(rolls[i])+'\t'+str(names[i])+'\t'+str((100*p)/(p+a))+'\n')
        
    def show_database(self):
        #To display attendance on specific date 
        date=str(self.yyyy.value())+str(self.mm.value())+str(self.dd.value())
        self.text.clear()
        temp = 'Roll\tName\t'+self.format_date(date)
        self.text.insertPlainText(temp+'\n')
        
        xyear = (int(self.subject[2])+1)//2
        query='SELECT * FROM YEAR{}'.format(xyear)
        c.execute(query)
        rolls = []
        names = []
        for row in c.fetchall():
            rolls.append(row[0])
            names.append(row[1])
                         
        for i in range(len(rolls)):
            query='SELECT Date, ['+ str(rolls[i]) + '] FROM {} where Date = {}'.format(self.subject, date)
            print (query)
            c.execute(query)
            temp = str(rolls[i])+'\t'+str(names[i])+'\t'
            for row in c.fetchall():
                temp += (row[1])
            self.text.insertPlainText(temp+'\n')
            
    def format_date(self, s):
        year = s[:4]
        month = s[4:6]
        date = s[6:]
        return date+'-'+month+'-'+year
    
if __name__ == '__main__':
    app = QtGui.QApplication([])
    gui = CheckAttendance()
    gui.show()
    app.exec_()
    c.close()
    conn.close()

