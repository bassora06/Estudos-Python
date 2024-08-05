def tratarErroDividirPorZeo(divisor):
    if divisor == 0:
        raise ZeroDivisionError('O divisor é zero, impossivel concluir conta')
    return True
    
def validarTipoDeVariavel(numero, divisor):
    if not isinstance(numero, (float, int)):
        raise TypeError(f'O valor {numero} não é inteiro')
    elif not isinstance(divisor, (int, float)):
        raise TypeError(f'O valor {divisor} não é inteiro')
    return True
    
def divide(numero, divisor):
    tratarErroDividirPorZeo(divisor)
    validarTipoDeVariavel(numero, divisor)

    return numero / divisor


print(divide(8, 2))

