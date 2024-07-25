class Carrinho():
    def __init__(self):
        self._produtos = []

    def total(self):
        return sum([p.preco for p in self._produtos])
    
    def listar_produtos(self):
        for produto in self._produtos: #lista os produtos da lista produtos 
            print(produto.nome, produto.preco)

    def inserirProdutos(self, *produtos):
        for produto in produtos:
            self._produtos.append(produto)

class Produto():
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


carrinho = Carrinho()
p1, p2, p3 = Produto('Caneta', 1.20),Produto ('Melancia', 5.00), Produto('Carrinho', 30.50)


carrinho.inserirProdutos(p1, p2, p3)
carrinho.listar_produtos()
print(f'\nO total dos produtos é: {carrinho.total()}')
