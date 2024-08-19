import sys
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QGridLayout, QMainWindow

app = QApplication(sys.argv)
window = QMainWindow()
centralWidget = QWidget()

window.setCentralWidget(centralWidget)

botao = QPushButton('Salvar')
botao.setStyleSheet('font-size: 15px; width: 10px;')

layout = QGridLayout()

layout.addWidget(botao, 1, 1, 1, 2)


def statusBarEscreva(statusBar):
    statusBar.showMessage('Você clicou no botão')



menuBar = window.menuBar()
primeiroMenu = menuBar.addMenu('Ola pessoa')
menuBar.setStyleSheet('text-align: center;')
primeiraAcao = primeiroMenu.addAction('Primeira ação')
primeiraAcao.triggered.connect(lambda: statusBarEscreva(statusBar))

statusBar = window.statusBar()
statusBar.showMessage('Ola mundo')


window.show()

app.exec()

