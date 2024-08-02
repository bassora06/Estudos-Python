string = 'lucas'

valoresDeString = string.__dir__

if hasattr(string, 'upper'):
    print('existe upper')
    print(string.upper())
else: 
    print('não existe upper')