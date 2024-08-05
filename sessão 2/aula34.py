try:
  8/2
except ZeroDivisionError as error:
    print('Erro: ', error)
    print()
else: 
   print('Isso executado caso não tenha dado nenhum erro')
   print()
finally:
   print('Isso sempre vai ser executado não importa oque aconteça')
