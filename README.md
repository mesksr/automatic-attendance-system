# Automated_Attendance_System

Automatic Attendance System is designed to collect and manage student’s attendance records from video camera devices installed in a class rooms. Based on the verification of student identification in the video cameras, attendance will be updated in data base. Attendance will be taken in every class at particular interval of time.

## GUI:
The GUI of this project "Automated Attendance System" has been made using PyQt4 module of Python. It is basically seperated into three 
windows:
1.Main Window
2.Registration Window
3.Attendance Window

## FACE EXTRACTION & FACE DETECTION:
The face detection and extraction part has been executed by the OpenCv(cv2) module of Python. Haar Casscade Classifiers have been used for 
frontal face detection.

## DATABASE HANDLING:
The database handling i.e. storing student's information and attendance has been done in this project using sqlite3 module in Python.

## IMAGE ENHANCEMENT:
The enhancement of image quality like adjusting brightness, sharpness ,etc will be done using PIL module in python 

## WORKING:
The program can be executed by running the main_window.py after you have installed libraries like PyQt4, cv2, numpy and PIL.The GUI will guide you to two windows one is the Registeration Window where a student can registered and the other is Attendance Window where attendance can be marked for a particular subject on a specific date.The other option is to check attendance for a subject on a given date.  

## Getting Started
To deploy this project on local machine you have to download complete code on your system.The program can be executed by running the main_window.py.
 
## Prerequisites
What things you need to install the software and how to install them
 
```
 Python 3.0 or later
 Python Libraries:
 * PIL
 * PyQt4
 * numpy
 * cv2
```
 
## Built With
 * [Python](https://www.python.org/) - The programming language used
 * [PyQt4](https://pypi.python.org/pypi/PyQt4) - GUI Management
 * [cv2](https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_image_display/py_image_display.html) - Face Recognisation
 
## Contributing
We will update the details soon.
 
## Versioning
We use [GitHub](http://github.com/) for versioning. 
 
## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details