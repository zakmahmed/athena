import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtGui import QIcon, QPixmap, QColor
from PyQt6.QtCore import QSize, Qt

class AthenaGUI(QMainWindow):
    def __init__(self):
        super(AthenaGUI, self).__init__()
        self.GuiInit()

    def GuiInit(self):
        self.setWindowTitle('Athena')
        self.setMinimumSize(QSize(200,300))

        self.label = QLabel()
        self.pixmap = QPixmap('icon.png')
        self.label.setPixmap(self.pixmap)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(self.label)

        self.myPalette = self.palette()
        self.myPalette.setColor(self.backgroundRole(), QColor(255,255,255))
        self.setPalette(self.myPalette)


        self.show()
        

    
app = QApplication(sys.argv)
window = AthenaGUI()
sys.exit(app.exec())