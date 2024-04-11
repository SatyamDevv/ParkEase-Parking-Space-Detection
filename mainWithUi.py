from PyQt5.QtWidgets import *
from PyQt5 import uic
import numpy as np
import spacePicker
import mainfile

class MyGUI(QMainWindow):
    def __init__(self):
        super().__init__()  # Correctly use super().__init__()
        uic.loadUi("D:\\Christ\\SEMESTER 4\\DBMS Project\\ParkEase\\mainUi.ui", self)
        self.show()
        self.createBox.clicked.connect(self.makebox)
        self.selectVideo.clicked.connect(self.selectvideo)
        self.userUi.clicked.connect(self.open_new_window)
        

    def makebox(self):
        spacePicker.runframes()
        print("Box created")

    def selectvideo(self):
        mainfile.determineSpot()
        print("Video selected")

    def open_new_window(self):
        #this window currently did not work
        print("User UI")
        self.new_window = NewWindow()  # Create a new instance of the new window class
        self.new_window.show()
        

class NewWindow(QGroupBox):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"D:\Christ\SEMESTER 4\DBMS Project\ParkEase\userUi.ui", self)
        self.freeSpot.setText("Free Spot\n"+ str(len(mainfile.posList)))
        self.available.setText("Available Spot\n"+ str(len(mainfile.posList)))
        self.totalSpot.setText("Total Spot\n"+ str(len(mainfile.posList)))
        self.totalSpot.setStyleSheet("QLabel { font-size: 20px; text-align: center; vertical-align: middle; font-weight: bold; background-color: blue; color: white; }")
        self.freeSpot.setStyleSheet("QLabel { font-size: 20px; text-align: center; vertical-align: middle; font-weight: bold; background-color: green; color: white; }")
        self.available.setStyleSheet("QLabel { font-size: 20px; text-align: center; vertical-align: middle; font-weight: bold; background-color: red; color: white; }")



def main():
    app = QApplication([])
    window = MyGUI()
    window.setWindowTitle("ParkEase") 
    app.exec_()

if __name__ == "__main__":
    main()


