#https://pyqtdarktheme.readthedocs.io/en/stable/how_to_use.html
import qdarktheme
from constants import *
    
qss = f"""
    QPushButton[cssClass="specialButton"] {{
        color: #fff;
        background: {PRIMARY_COLOR};
    }}
    QPushButton[cssClass="specialButton"]:hover {{
        color: #fff;
        background: {PRIMARY_COLOR_DARK_ONE};
    }}
    QPushButton[cssClass="specialButton"]:pressed {{
        color: #fff;
        background: {PRIMARY_COLOR_DARK_TWO};
    }}
"""
def setupTheme():
    qdarktheme.setup_theme(theme='dark',corner_shape='rounded',\
        custom_colors={"[dark]": {"primary":PRIMARY_COLOR},\
            '[light]':{'primary':PRIMARY_COLOR}}, additional_qss=qss)