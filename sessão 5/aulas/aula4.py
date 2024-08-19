import sys
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QGridLayout, QMainWindow

app = QApplication(sys.argv)
window = QMainWindow()
centralWidget = QWidget()
layout = QGridLayout()



window.setCentralWidget(centralWidget) # setando o central widget no QMainwindow 

botao = QPushButton('Salvar')
botao.setStyleSheet('font-size: 15px; width: 10px;')



layout.addWidget(botao, 1, 1, 1, 2)


def statusBarEscreva(statusBar):
    statusBar.showMessage('Você clicou no botão')



menuBar = window.menuBar() # criando o menu
primeiroMenu = menuBar.addMenu('Ola pessoa') #Botão de menu
menuBar.setStyleSheet('text-align: center;')

primeiraAcao = primeiroMenu.addAction('Botão 1 dentro do menu') # Botão de ação dentro do botão de menu principal
primeiraAcao.hovered.connect(lambda: statusBarEscreva(statusBar)) # Botão primeira ação recebe um método

statusBar = window.statusBar() # cria uma status bar
statusBar.showMessage('Ola mundo') # Escreve algo na status bar


window.show()

app.exec()

