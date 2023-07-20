from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont # проверка типов вводимых значений
from PyQt5.QtWidgets import (
        QApplication, QWidget,
        QHBoxLayout, QVBoxLayout, QGridLayout,
        QGroupBox, QRadioButton,
        QPushButton, QLabel, QListWidget, QLineEdit)
 
from instr import *
from final_win import *
 
class TestWin(QWidget):
    def __init__(self):
        ''' окно, в котором проводится опрос '''
        super().__init__()
    
        # создаём и настраиваем графические элементы:
        self.initUI()
    
        #устанавливает связи между элементами
        self.connects()
    
        #устанавливает, как будет выглядеть окно (надпись, размер, место)
        self.set_appear()
        
        # старт:
        self.show()
    
    ''' устанавливает, как будет выглядеть окно (надпись, размер, место) '''
    def set_appear(self):
        pass
    
    def initUI(self):
        ''' создаёт графические элементы '''
        pass
    
    def next_click(self):
        pass
    
    def connects(self):
        pass
