from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import QTimer
import spacePicker
import mainfile
import threading

class MyGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"UI\mainUi.ui", self)
        self.show()
        self.createBox.clicked.connect(self.makebox)
        self.selectVideo.clicked.connect(self.selectvideo)
        self.userUi.clicked.connect(self.open_new_window)

    def makebox(self):
        spacePicker.runframes()
        print("Box created")

    def selectvideo(self):
        # Start the determineSpot function in a separate thread
        thread = threading.Thread(target=mainfile.determineSpot)
        thread.start()
        print("Video selected")

    def open_new_window(self):
        self.new_window = NewWindow()
        self.new_window.show()

class NewWindow(QGroupBox):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"UI\userUi.ui", self)

        # Create a timer to update the labels periodically
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_labels)
        self.timer.start(1000)  # Update every 1 second

    def update_labels(self):
        space_counter = mainfile.shared_space_counter.value
        total_spots = len(mainfile.posList)
        available_spots = total_spots - space_counter

        self.freeSpot.setText(f"Free Spot\n{space_counter}")
        self.available.setText(f"Occupied Spot\n{available_spots}")
        self.totalSpot.setText(f"Total Spot\n{total_spots}")

        # Set the style sheets for the labels
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