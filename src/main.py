from PySide6.QtWidgets import QApplication
from main_window import Main_Window
from PySide6.QtGui import QIcon
import sys
import constants
from display import Display
from label_info import Label_info
from styles import setupTheme
from buttons import Button, ButtonsGrid

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main_Window()
    setupTheme()
    window.setWindowIcon(QIcon(str(constants.WINDOW_ICON_THEME)))
    app.setWindowIcon(window.icon)
    
    label = Label_info('Label')
    window.add_to_VLayuot(label)
    
    display = Display()
    window.add_to_VLayuot(display)
    
    #Grid
    buttons_grid = ButtonsGrid(display,label)
    window.v_layout.addLayout(buttons_grid)
    
    window.adjustFixedSize()
    window.show()
    app.exec()