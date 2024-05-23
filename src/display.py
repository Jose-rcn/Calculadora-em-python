from PySide6.QtWidgets import QLineEdit
from constants import *
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QKeyEvent
from util import is_empty,is_num_or_dot
class Display(QLineEdit):
    eq_pressed = Signal()
    del_pressed = Signal()
    esc_pressed = Signal()
    num_pressed = Signal(str)
    operator_pressed = Signal(str)
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config_style()
        
    def config_style(self):
        self.setStyleSheet(f'font-size:{BIG_FONT_SIZE}px;')
        self.setMinimumHeight(2 * BIG_FONT_SIZE)
        self.setMinimumWidth(MINIMUN_WIDHT)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*[DEFAULT_TXT_MARGIN for _ in range(4)])
        
    def keyPressEvent(self, event: QKeyEvent) -> None:
        text = event.text().strip()
        KEYS = Qt.Key
        key = event.key()
        is_enter = key in [KEYS.Key_Enter,KEYS.Key_Return, KEYS.Key_Equal]
        is_delete =  key in [KEYS.Key_Backspace,KEYS.Key_Delete]
        is_esc = key in [KEYS.Key_Escape,KEYS.Key_C]
        is_operator = key in [
            KEYS.Key_Plus,KEYS.Key_Minus,KEYS.Key_Slash,KEYS.Key_Asterisk,
            KEYS.Key_P]
        if is_enter:
            self.eq_pressed.emit()
            return event.ignore()
        if is_delete:
            self.del_pressed.emit()
            return event.ignore()
        if is_esc:
            self.esc_pressed.emit()
            return event.ignore()
        if is_operator:
            if text.lower() == 'p':
                text = '^'
            self.operator_pressed.emit(text)
            return event.ignore()
        if is_empty(text):
            return event.ignore()
        if is_num_or_dot(text):
            self.num_pressed.emit(text)
            return event.ignore()
        
        