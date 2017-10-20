import cv2
import sqlite3
from PyQt4 import QtGui,QtCore


class RegistrationWindow(QtGui.QMainWindow):
    #Registration window for student registration
      
    def __init__(self):
        super(RegistrationWindow, self).__init__()
        
        #Creating Registration Window 
        self.setGeometry(300,50,800,600)
        self.setWindowTitle("Registration")
        self.setWindowIcon(QtGui.QIcon('other_images/logo.png'))

        #Heading
        h=QtGui.QLabel(self)
        h.setAlignment(QtCore.Qt.AlignCenter)
        h.setGeometry(QtCore.QRect(100,30,600,60))
        h.setStyleSheet("QLabel { background-color : blue;color :white ; }")
        font=QtGui.QFont("Times",20,QtGui.QFont.Bold)
        h.setFont(font)
        h.setText("REGISTRATION")

        #Pseudo photo ID to be replaced by Student's Photo
        self.pic=QtGui.QLabel(self)
        self.pic.setGeometry(50,120,320,320)
        self.pic.setPixmap(QtGui.QPixmap("other_images/default.png"))

        #Button for opening Webcam and take photo 
        b=QtGui.QPushButton(self)
        b.setText("CLICK")
        b.setFont(QtGui.QFont("Times",12,QtGui.QFont.Bold))
        b.setGeometry(100,420,100,30)
        b.clicked.connect(self.take_photo)

        #SET OF ENTRIES
        #Taking Student's Name
        l1=QtGui.QLabel(self)
        l1.setAlignment(QtCore.Qt.AlignCenter)
        l1.setGeometry(QtCore.QRect(310,150,130,30))
        l1.setStyleSheet("QLabel { background-color : gray;color :black ; }")
        font=QtGui.QFont("Times",14,QtGui.QFont.Bold)
        l1.setFont(font)
        l1.setText("NAME")

        self.e1=QtGui.QLineEdit(self)
        self.e1.setGeometry(450,150,300,30)
        self.e1.setAlignment(QtCore.Qt.AlignCenter)
        font1=QtGui.QFont("Arial",14)
        self.e1.setFont(font1)

        #Taking Student's Registration Number
        l2=QtGui.QLabel(self)
        l2.setAlignment(QtCore.Qt.AlignCenter)
        l2.setGeometry(QtCore.QRect(310,250,130,30))
        l2.setStyleSheet("QLabel { background-color : gray;color :black ; }")
        l2.setFont(font)
        l2.setText("ROLL NO.")

        self.e2=QtGui.QLineEdit(self)
        self.e2.setGeometry(450,250,300,30)
        self.e2.setAlignment(QtCore.Qt.AlignCenter)
        self.e2.setFont(font1)

        #Taking Student's Year of Study
        l3=QtGui.QLabel(self)
        l3.setAlignment(QtCore.Qt.AlignCenter)
        l3.setGeometry(QtCore.QRect(310,350,130,30))
        l3.setStyleSheet("QLabel { background-color : gray;color :black ; }")
        l3.setFont(font)
        l3.setText("YEAR")
      
        self.e3=QtGui.QLineEdit(self)
        self.e3.setGeometry(450,350,300,30)
        self.e3.setAlignment(QtCore.Qt.AlignCenter)
        self.e3.setFont(font1)

        #Button for clearing fields 
        b2=QtGui.QPushButton(self)
        b2.setText("RESET")
        b2.setFont(QtGui.QFont("Times",12,QtGui.QFont.Bold))
        b2.setGeometry(650,450,100,30)
        b2.setStyleSheet("QPushButton { background-color : red ;color : white ; }")
        self.entries=[self.e1,self.e2,self.e3]
        b2.clicked.connect(self.erase)

        #Label for displaying message
        self.l4=QtGui.QLabel(self)
        self.l4.setAlignment(QtCore.Qt.AlignCenter)
        self.l4.setStyleSheet("QLabel {  color:green ; }")
        self.l4.setFont(QtGui.QFont('Times',13))
        
        #Button for submission of data and storing in database 
        b1=QtGui.QPushButton(self)
        b1.setText("SUBMIT")
        b1.setFont(QtGui.QFont("Times",12,QtGui.QFont.Bold))
        b1.setGeometry(520,450,100,30)
        b1.setStyleSheet("QPushButton { background-color : green;color : white ; }")
        b1.clicked.connect(self.store_in_database)
            
    def erase(self):
        #function for clearing fields and changing to default
        for entry in self.entries:
            entry.clear()
        self.pic.setPixmap(QtGui.QPixmap("other_images/default.png"))
        self.l4.setText("")
    
    def take_photo(self):
        #Function for clicking,displaying and storing photo
        check_value = self.check()
        if (check_value == 1):
            self.l4.setGeometry(QtCore.QRect(40,500,250,30))
            self.l4.setText("Invalid Name")
        elif (check_value == 2):
            self.l4.setGeometry(QtCore.QRect(40,500,250,30))
            self.l4.setText("Roll - Out of Range")
        elif (check_value == 3):
            self.l4.setGeometry(QtCore.QRect(40,500,250,30))
            self.l4.setText("Year should be between 1 to 4")
        else:
            face_cascade=cv2.CascadeClassifier('support_files/haarcascade_frontalface_default.xml')
            cap=cv2.VideoCapture(0)
            while True:
                ret,img=cap.read()
                gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                face=face_cascade.detectMultiScale(gray,1.3,5)
                for (x,y,w,h) in face:
                    roi_color=img[y:y+h,x:x+w]
                    cv2.imwrite(str(r'C:\\Users\\mesksr\\Documents\\GitHub\\automatic-attendance-system\\registration_images\\Year' +
                                 str(self.e3.text())+'\\'+str(self.e2.text())+'.png'),roi_color)
                cv2.imshow('img',img)
                k=cv2.waitKey(30) & 0xff
                if k==27:
                    break
            cap.release()
            cv2.destroyAllWindows()
            self.pic.setPixmap(QtGui.QPixmap(str(r'C:\\Users\\mesksr\\Documents\\GitHub\\automatic-attendance-system\\registration_images\\Year' +
                                             str(self.e3.text())+'\\'+str(self.e2.text())+'.png')))

    def store_in_database(self):
        #Function for storing information in database
        check_value = self.check()
        print ('>>', check_value)
        if (check_value == 0):
            conn=sqlite3.connect('Attendance System.db')
            c=conn.cursor()
            c.execute('CREATE TABLE IF NOT EXISTS YEAR' + str(self.e3.text()) + ' (Roll INT, Name TEXT)')
            (name,regno,year)=(self.e1.text(),int(self.e2.text()),int(self.e3.text()))
            c.execute('INSERT INTO YEAR' + str(self.e3.text()) + ' (Roll,Name) VALUES(?,?)',(regno,name))
            conn.commit()
            c.close()
            conn.close()
            #Displaying message after successful submission 
            self.l4.setGeometry(QtCore.QRect(40,500,250,30))
            self.l4.setText("Successfully Registered")
        elif (check_value == 1):
            self.l4.setGeometry(QtCore.QRect(40,500,250,30))
            self.l4.setText("Invalid Name")
        elif (check_value == 2):
            self.l4.setGeometry(QtCore.QRect(40,500,250,30))
            self.l4.setText("Roll - Out of Range")
        elif (check_value == 3):
            self.l4.setGeometry(QtCore.QRect(40,500,250,30))
            self.l4.setText("Year should be between 1 to 4")
        elif (check_value == 4):
            self.l4.setGeometry(QtCore.QRect(40,500,250,30))
            self.l4.setText("Click again please.")
            

    def check(self):
        name = self.e1.text()
        if (len(name) == 0):
            return 1
        
        for i in range(10):
            if (str(i) in name):
                return 1
        
        try:
            roll = int(self.e2.text())
            if (roll < 1 or roll > 100):
                return 2
        except:
            return 2
        
        try:
            year = int(self.e3.text())
            if (year < 1 or year > 4):
                return 3
        except:
            return 3
            
        try:
            img = cv2.imread(r'C:\\Users\\mesksr\\Documents\\GitHub\\automatic-attendance-system\\registration_images\\Year' +
                            str(self.e3.text())+'\\'+str(self.e2.text())+'.png', 0)
            face_cascade=cv2.CascadeClassifier('support_files/haarcascade_frontalface_default.xml')
            faces = face_cascade.detectMultiScale(img, 1.3, 5)
            print (len(faces), 'face(s) detected')
            if (len(faces) != 1):
                return 4
        except:
            return 4
        
        return 0
    

if __name__ == '__main__':  
    app = QtGui.QApplication([])
    gui = RegistrationWindow()
    gui.show()
    app.exec_()
