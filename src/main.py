from PySide6.QtWidgets import QWidget, QMainWindow, QVBoxLayout, QApplication, QLabel
from main_window import Main_Window
from PySide6.QtGui import QIcon
import sys
import constants
from display import Display
from label_info import Label_info
from styles import setupTheme

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main_Window()
    setupTheme()
    window.setWindowIcon(QIcon(str(constants.WINDOW_ICON_THEME)))
    app.setWindowIcon(window.icon)
    
    label = Label_info('asdsddsad')
    window.add_to_VLayuot(label)
    
    display = Display('0')
    window.add_to_VLayuot(display)
    
    
    window.adjustFixedSize()
    window.show()
    app.exec()