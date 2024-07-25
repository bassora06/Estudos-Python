class Caneta():

    def __init__(self, cor, tampa):
        self.corTinta = cor
        self.corTampa = tampa

    #getter normal, usado em todas as outras linguagens
    # def getCor(self):
    #     return self.CorTinta


    #getter em pythonico
    #Ele faz uma função, essa função é executada como um atributo
    @property
    def getCor(self):
        return self.corTinta
    
    @property
    def getTampa(self):
        return self.corTampa
    

c1 = Caneta('Azul', 'redonda')

print(c1.getCor, c1.getTampa)
print(c1.getCor, c1.getTampa)
print(c1.getCor, c1.getTampa)
print(c1.getCor, c1.getTampa)
print(c1.getCor, c1.getTampa)



    