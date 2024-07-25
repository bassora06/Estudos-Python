import sys
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QGridLayout

app = QApplication(sys.argv)

botao = QPushButton('Salvar')
botao.setStyleSheet('font-size: 15px; width: 10px;')

botao2 = QPushButton('Deletar')
botao2.setStyleSheet('font-size: 15px; width: 10px;')


centralWidget = QWidget()
layout = QGridLayout()

centralWidget.setLayout(layout)

layout.addWidget(botao2, 1, 1)
layout.addWidget(botao, 1, 2)


centralWidget.show()

app.exec()

