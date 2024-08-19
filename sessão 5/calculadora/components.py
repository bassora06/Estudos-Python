from PySide6.QtWidgets import  QPushButton, QLineEdit, QGridLayout, QWidget
from variables import bigFontSize, defaultMargin , minimunHeight , minimunWidth, mediumFontSize 
from PySide6.QtCore import Qt
from utils import isNumOrDotRegex, isEmpty

class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        font = self.font()
        font.setPixelSize(mediumFontSize)
        self.setFont(font)
        self.setMinimumSize(75, 75)

class ButtonsGrid(QGridLayout):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        
        self._gridMask= [
            ['C', '<', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['', '0', '.', '='],
        ]
        self._makeGrid()


    def _makeGrid(self):
        for rowNumber, rowData in enumerate(self._gridMask):
            for colNumber, buttonText in enumerate(rowData):
                button = Button(buttonText)

                if not isNumOrDotRegex(buttonText) and not isEmpty(buttonText):
                    button.setProperty('cssClass', 'specialButton')

                self.addWidget(button, rowNumber, colNumber)
                button.clicked.connect(self._insertButtonTextDisplay)


    def _insertButtonTextDisplay(self):
        print(123)
    

class Display(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        margins = [defaultMargin for _ in range(4)]
        self.setStyleSheet(f'font-size: {bigFontSize}px;')
        self.setMinimumHeight(minimunHeight)
        self.setMinimumWidth(minimunWidth)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*margins)