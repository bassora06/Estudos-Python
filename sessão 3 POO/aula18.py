# class Pessoa(str):
#     def upper(self):
#         return 'ABC'


# p1 = Pessoa('Lucas')
# print(p1.upper())

class A:
    atributoA = 'valor A'

    def metodo(self):
        print('A')

class B(A):
    atributoB = 'valor B'

    def metodo(self):
        print('B')

class C(B):
    atributoC = 'valor C'

    def metodo(self):
        print('C')


a = A()
b = B()
c = C()

a.metodo()
print(a.atributoA)

b.metodo()
print(b.atributoB)

c.metodo()
print(c.atributoC)

