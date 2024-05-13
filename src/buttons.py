from PySide6.QtWidgets import QPushButton, QGridLayout, QWidget
from constants import *
from util import is_num_or_dot, is_empity, is_valid_number
import math

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from display import Display
    from label_info import Label_info
    from main_window import Main_Window

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
    def __init__(self,display:'Display',info:'Label_info',m_window:'Main_Window',*args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.main_window = m_window
        self.display = display
        self.info = info
        self._equation = ''
        self.left = None
        self.right = None
        self.operator = None
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
                    self._config_special_button(button=btn)
                btn_slot = self.make_slot(self.insert_text_to_display,btn)
                self._conect_button_clicked(btn,btn_slot)
                
    def insert_text_to_display(self,btn):
        btn_txt = btn.text()
        display_text = self.display.text() + btn_txt
        if is_valid_number(display_text):
            self.display.insert(btn_txt)
    def _conect_button_clicked(self, button, slot):
        button.clicked.connect(slot)
        
    def make_slot(self,method,*args, **kwargs):
        def real_slot():
            method(*args, **kwargs)
        return real_slot
    
    def _config_special_button(self,button:Button):
        text = button.text()
        if text == 'C':
            self._conect_button_clicked(button,self._clear)
        if text in '+-*/^':
            slot_operators = self.make_slot(self._operator_clicked,button)
            self._conect_button_clicked(button,slot_operators)
        if text in '=':
            self._conect_button_clicked(button,self._eq)
        if text == '◀':
            self._conect_button_clicked(button,self.display.backspace)
            
    def _clear(self):
        self.display.clear()
        self.left = None
        self.right = None
        self.operator = None
        self.equation = ''
        
    def _operator_clicked(self,button):
        btn_text = button.text()
        display_text = self.display.text()
        
        self.display.clear()
        #clicou no operador sem nada escrito, ou coisas invalidas
        if not is_valid_number(display_text) and self.left is None:
            self._show_error('Digita alguma coisa cabrunco')
            return
        if self.left is None:
            self.left = float(display_text)
            
        self.operator = btn_text
        self.equation = f'{self.left} {self.operator}'
        
    def _eq(self):
        display_text = self.display.text()
        if not is_valid_number(display_text):
            self._show_error('Digita alguma coisa cabrunco')
            return
        if self.left is None:
            return
        self.right = float(display_text)
        self.equation = f'{self.left} {self.operator} {self.right}'
        result = 'error'
        try:
            if '^' in self.equation and isinstance(self.left,float):
                result = math.pow(self.left,self.right)
            else:
                result = eval(self.equation.replace('^','**'))
        except ZeroDivisionError:
            self._show_error('Divisão por zero')
        except OverflowError:
            print('Numero grande pa karalho')
        self.display.clear()
        self.info.setText(f'{self.equation} = {result}')
        self.left = result
        self.right = None
        if result =='error':
            self.left = None
            
    def _show_error(self,text):
        msg_box = self.main_window.add_message_box()
        msg_box.setText(text)
        msg_box.setIcon(msg_box.Icon.Critical)
        msg_box.exec()