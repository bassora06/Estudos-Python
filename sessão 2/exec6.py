import copy

from dados import produtos



novosProdutos = [
    {**p, 'preço': round(p['preço']* 1.1, 2)}
      for p in copy.deepcopy(produtos)
]

produtosOrdenadosPorNome = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['nome']
)

produtosOrdenadosPorPreco = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['preço']
)

    
print(*produtos, sep='\n')
print()
print(*novosProdutos, sep='\n')
print()
print(*produtosOrdenadosPorNome, sep='\n')
print()
print(*produtosOrdenadosPorPreco, sep='\n')