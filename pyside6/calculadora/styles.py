import qdarkstyle
from variables import (darkerPrimaryColor, darkestPrimaryColor,
                       primaryColor)
 
qss = f"""
    PushButton[cssClass="specialButton"] {{
        color: #fff;
        background: {primaryColor};
        border-radius: 5px;
    }}
    PushButton[cssClass="specialButton"]:hover {{
        color: #fff;
        background: {darkerPrimaryColor};
    }}
    PushButton[cssClass="specialButton"]:pressed {{
        color: #fff;
        background: {darkestPrimaryColor};
    }}
"""
 
 
def setupTheme(app):
    # Aplicar o estilo escuro do qdarkstyle
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())
 
    # Sobrepor com o QSS personalizado para estilização adicional
    app.setStyleSheet(app.styleSheet() + qss)