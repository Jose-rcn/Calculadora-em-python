from PySide6.QtWidgets import QWidget, QMainWindow, QVBoxLayout, QMessageBox
from PySide6.QtGui import QIcon
import constants

class Main_Window(QMainWindow):
    def __init__(self, parent: QWidget | None = None,*args, **kwargs) -> None:
        super().__init__(parent,*args, **kwargs)
        self.cw = QWidget()
        self.v_layout = QVBoxLayout()
        self.cw.setLayout(self.v_layout)
        self.setCentralWidget(self.cw)
        self.setWindowTitle('Calculadora')
        #icon
        self.icon = QIcon(str(constants.WINDOW_ICON_THEME))
        self.setWindowIcon(self.icon)
    def adjustFixedSize(self):
        self.adjustSize()
        self.setFixedSize(self.width(),self.height())
    def add_to_VLayuot(self, widget:QWidget):
        self.v_layout.addWidget(widget)
    def add_message_box(self):
        msg_box = QMessageBox(self)
        return msg_box