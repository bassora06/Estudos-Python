import sys
from components import Display, ButtonsGrid
from info import Info
from mainWindow import MainWindow
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from styles import setupTheme
from variables import WINDOWS_ICON_PATH

if __name__ == '__main__':
    
    # Cria a aplicação
    app = QApplication(sys.argv)
    setupTheme(app)
    window = MainWindow()
 
    # Define o ícone
    icon = QIcon(str(WINDOWS_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)
 
    # Info
    info = Info('Sua conta')
    window.addWidgetToVlayout(info)
 
    # Display
    display = Display()
    window.addWidgetToVlayout(display)

    # Grid
    buttonsGrid = ButtonsGrid()
    window.vLayout.addLayout(buttonsGrid)

    buttonsGrid._makeGrid()
    #buttonsGrid.addWidget(Button('4', 1, 0, 1, 1)) # Linha, coluna, linha que se expande, coluna que se expande
 
    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()