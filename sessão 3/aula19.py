class A():
    ...

    def quem_eu(self):
        print('A')

class B(A):
    ...

    def quem_eu(self):
        print('B')

class C(A):
    ...

    def quem_eu(self):
        print('C')

class D(B, C):  #chama a primeira class citada no caso a classe B
    ...

    def quem_eu(self):
        super().quem_eu()
        print('D')


d = D()
d.quem_eu()