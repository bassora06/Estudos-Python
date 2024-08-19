import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QVBoxLayout, QMainWindow, QApplication, QWidget, QLabel

class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        
        
        # Layout básico
        self.cw = QWidget()
        self.setCentralWidget(self.cw)
        self.vLayout = QVBoxLayout()

        # Título da janela
        self.setWindowTitle('Calculadora')


    def adjustFixedSize(self):
            # Ultima coisa a ser feita
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())
        
    def addWidgetToVlayout(self, widget: QWidget):
        self.vLayout.addWidget(widget)


        self.cw.setLayout(self.vLayout)

    def addLabel(self, text):
        label = QLabel(text)
        label.setStyleSheet('font-size: 100px; font-family: elephant;')
        self.addWidgetToVlayout(label)