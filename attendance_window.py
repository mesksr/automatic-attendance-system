
from check_attendance import CheckAttendance
from PyQt4 import QtGui,QtCore

class AttendanceWindow(QtGui.QMainWindow):
    #Attendance Window
    def __init__(self):
        super(AttendanceWindow, self).__init__()
        self.setGeometry(300,50,800,600)
        self.setWindowTitle("Attendance")
        self.setWindowIcon(QtGui.QIcon('other_images/logo.png'))

        #Heading
        h=QtGui.QLabel(self)
        h.setAlignment(QtCore.Qt.AlignCenter)
        h.setGeometry(QtCore.QRect(200,20,400,50))
        h.setStyleSheet("QLabel { background-color : blue;color :white ; }")
        font=QtGui.QFont("Times",20,QtGui.QFont.Bold)
        h.setFont(font)
        h.setText("ATTENDANCE")

        #Label and Subject code entry
        l=QtGui.QLabel(self)
        l.setAlignment(QtCore.Qt.AlignCenter)
        l.setGeometry(QtCore.QRect(275,140,250,30))
        l.setStyleSheet("QLabel { background-color:green;color: white;}")
        font=QtGui.QFont("Times",16,QtGui.QFont.Bold) 
        l.setFont(font)
        l.setText("ENTER SUB-CODE")

        self.e = QtGui.QLineEdit(self)
        self.e.setGeometry(275,175,250,50)
        self.e.setAlignment(QtCore.Qt.AlignCenter)
        self.e.setFont(QtGui.QFont("Times",18,QtGui.QFont.Bold))

        #Recording Button
        b1=QtGui.QPushButton(self)
        b1.setText("RECORD AND MARK")
        b1.setStyleSheet("QPushButton { background-color : gray;color : black ; }")
        b1.setFont(font)
        b1.setGeometry(250,300,300,50)
        b1.clicked.connect(self.record_and_mark)

        #Check Attendance button to check specific subject's Attendance
        b2=QtGui.QPushButton(self)
        b2.setText("CHECK ATTENDANCE")
        b2.setStyleSheet("QPushButton { background-color : gray;color : black ; }")
        b2.setFont(font)
        b2.setGeometry(250,425,300,50)
        b2.clicked.connect(self.create_check_attendance)
        
    def create_check_attendance(self):
        #To check Validity of Subject Code 
        sub=["IT301","IT302"] #TO DO - GET THESE FROM TABLE
        if self.e.text() in sub:
            self._check_attendance = CheckAttendance(self.e.text())
            self._check_attendance.show()

    def record_and_mark(self):
        self.record() #to record the video and save it to folder 'videos'
        self.mark()

    def mark(self):
        
            
if __name__ == '__main__':
    app = QtGui.QApplication([])
    gui = AttendanceWindow()
    gui.show()
    app.exec_()
