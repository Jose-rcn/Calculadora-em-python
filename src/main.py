from PySide6.QtWidgets import QApplication
from main_window import Main_Window
from PySide6.QtGui import QIcon
import sys
import constants
from display import Display
from label_info import Label_info
from buttons import ButtonsGrid

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main_Window()
    app.setWindowIcon(window.icon)
    window.setWindowIcon(window.icon)
    window.setWindowIcon(QIcon(str(constants.WINDOW_ICON_THEME)))
    
    label = Label_info('')
    window.add_to_VLayuot(label)
    
    display = Display()
    window.add_to_VLayuot(display)
    
    #Grid
    buttons_grid = ButtonsGrid(display,label,window)
    window.v_layout.addLayout(buttons_grid)
    
    window.adjustFixedSize()
    window.show()
    app.exec()