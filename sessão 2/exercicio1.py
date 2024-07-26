
def multiplicacao(*args):
    total = 1
    for i in args:
        total *= i
    return total

total = multiplicacao(4, 2, 3, 4, 5)
print(total)
