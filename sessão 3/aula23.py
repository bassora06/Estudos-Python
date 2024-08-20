class MyError(Exception):
    ...

class OtherError(Exception):
    ...

def levantar():
    exception_ = MyError('A', 'b', 'c')
    exception_.add_note('Você errou isso')
    raise exception_

try:
    levantar()
except MyError as error:
    print(error.__class__.__name__)
    print(error.args)
    print()
    raise