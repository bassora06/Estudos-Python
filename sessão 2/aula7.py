x, y, *resto = 1, 2, 3, 4

# print(x, y, resto)

# def somar(x , y):
#     return x + y

def soma(*args):
    total = 0
    for i in args:
        print(total)
        total += 1
        print(i, total)
        
        

soma(1, 2, 3, 4, 5)