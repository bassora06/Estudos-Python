from log import LogPrintMixin

class Eletronico():
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if  not self._ligado:
            print('Ligando...')
            self._ligado = True


    def desligar(self):
        if  self._ligado:
            print('Desligando...')
            self._ligado = False





class Smartphone(Eletronico, LogPrintMixin):
    
    def ligar(self):
        super().ligar()

        if self._ligado:
            msg = f'{self._nome} está ligado'
            self.logSucess(msg)
    
    def desligar(self):
        super().ligar()

        if self._ligado:
            msg = f'{self._nome} está desligado'
            self.logError(msg)
    
     