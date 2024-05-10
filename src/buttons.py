from PySide6.QtWidgets import QPushButton, QGridLayout, QWidget
from constants import *
from util import is_num_or_dot, is_empity, is_valid_number

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from display import Display
    from label_info import Label_info

class Button(QPushButton):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config_style()
        
    def config_style(self):
        font = self.font()
        font.setPixelSize(BIG_FONT_SIZE)
        self.setFont(font)
        
        self.setMinimumSize(MINIMUN_BTN_W,MINIMUN_BTN_H)
        
class ButtonsGrid(QGridLayout):
    def __init__(self,display:'Display',info:'Label_info',*args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.display = display
        self.info = info
        self._equation = ''
        self._grid_mask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['',  '0', '.', '='],
        ]
        self.make_grid()
    @property
    def equation(self):
        return self._equation
    @equation.setter
    def equation(self,value):
        self._equation = value
        self.info.setText(value)
    def make_grid(self):
        for i,row in enumerate(self._grid_mask):
            for j,button_txt in enumerate(row):
                btn = Button(button_txt)
                self.addWidget(btn,i,j)
                if not is_num_or_dot(button_txt) and not is_empity(button_txt):
                    btn.setProperty('cssClass','specialButton')
                btn_slot = self.make_display_connection(self.insert_text_to_display,btn)
                btn.clicked.connect(btn_slot)
                
    def insert_text_to_display(self,btn):
        btn_txt = btn.text()
        display_text = self.display.text() + btn_txt
        if is_valid_number(display_text):
            self.display.insert(btn_txt)
        
    def make_display_connection(self,method,*args, **kwargs):
        def real_slot():
            method(*args, **kwargs)
        return real_slot