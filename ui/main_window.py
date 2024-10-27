from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow,QApplication
from window import Ui_MainWindow
import sys
class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.Send.clicked.connect(self.imprime_line_text)
    def imprime_line_text(self):
        print(self.lineEdit.text())
        self.result.setText(self.lineEdit.text())
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()