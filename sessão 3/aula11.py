class Caneta():

    def __init__(self, cor, corTampa):
        self._cor = cor
        self._corTampa = corTampa

    # Quando um atributo começa com _ significa que não é para utiliza-lo
    # atributo que começa com _ é bascicamente um atributo privado em python
    

    #getter do atributo privado _cor
    @property 
    def cor(self):
        print('getter cor')
        return self._cor
    

    @cor.setter
    def cor(self, valor):
        print('Setter cor')
        self._cor = valor


    @property
    def corTampa(self):
        print('getter cor tampa')
        return self._corTampa
    

    @corTampa.setter
    def corTampa(self, valor):
        print('Setter cor tampa')
        self._corTampa = valor


    
    


caneta = Caneta('Azul','Azul')
caneta.cor = 'Rosa'
caneta.corTampa = 'Preta'

print(caneta.cor, caneta.corTampa)
    

