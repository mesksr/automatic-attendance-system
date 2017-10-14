from check_attendance import CheckAttendance
from PyQt4 import QtGui,QtCore

class AttendanceWindow(QtGui.QMainWindow):
    #Attendance Window
    def __init__(self):
        super(AttendanceWindow, self).__init__()
        self.setGeometry(300,50,800,600)
        self.setWindowTitle("Attendance")
        self.setWindowIcon(QtGui.QIcon('logo1.png'))

        #Heading
        h=QtGui.QLabel(self)
        h.setAlignment(QtCore.Qt.AlignCenter)
        h.setGeometry(QtCore.QRect(200,20,400,50))
        h.setStyleSheet("QLabel { background-color : blue;color :white ; }")
        font=QtGui.QFont("Times",20,QtGui.QFont.Bold)
        h.setFont(font)
        h.setText("ATTENDANCE")

        b1=QtGui.QPushButton(self)
        b1.setText("RECORD & MARK")
        b1.setStyleSheet("QPushButton { background-color : gray;color : black ; }")
        b1.setFont(QtGui.QFont("Times",16,QtGui.QFont.Bold))
        b1.setGeometry(250,200,300,50)
        b1.clicked.connect(self.record_video)

        b2=QtGui.QPushButton(self)
        b2.setText("CHECK ATTENDANCE")
        b2.setStyleSheet("QPushButton { background-color : gray;color : black ; }")
        b2.setFont(QtGui.QFont("Times",16,QtGui.QFont.Bold))
        b2.setGeometry(250,350,300,50)
        b2.clicked.connect(self.create_check_attendance)
        
    def create_check_attendance(self):
        self._check_attendance = CheckAttendance()
        self._check_attendance.show()
        self.close()

    def record_video(self):
        #record()
        #snap()
        #extract_faces()
        #mark()
        pass
               
if __name__ == '__main__':
    app = QtGui.QApplication([])
    gui = AttendanceWindow()
    gui.show()
    app.exec_()
