import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QSystemTrayIcon
from PyQt6.QtGui import QIcon, QPixmap, QColor
from PyQt6.QtCore import QSize, Qt
import os


imagePath = 'Athena/icon.png'

class AthenaGUI(QMainWindow):
    def __init__(self):
        super(AthenaGUI, self).__init__()
        self.guiInit()

    def guiInit(self):
        self.setWindowTitle('Athena')
        self.setMinimumSize(QSize(200,300))     

        self.myPalette = self.palette()
        self.myPalette.setColor(self.backgroundRole(), QColor(255,255,255))
        self.setPalette(self.myPalette)


        
        

    
app = QApplication(sys.argv)
app.setWindowIcon(QIcon(imagePath))
window = AthenaGUI()
window.show()
sys.exit(app.exec())