# Still working on this.

from PyQt6.QtWidgets import QApplication, QWidget
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Learning PyQT")






app = QApplication([])
window = Window()
window.show()
sys.exit(app.exec())