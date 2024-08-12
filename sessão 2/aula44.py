from itertools import count

c1 = count(0, 8)
c2 = count(step=8, start=8)# começa no 8 e vai de 8 em 8
r1 = range(0, 100, 8)

print('c1', hasattr(c1, '__iter__'))
print('c1', hasattr(c1, '__next__'))
print('r1', hasattr(r1, '__iter__'))
print('r1', hasattr(r1, '__next__'))

print('Count')
for i in c1:
    if i >= 100:
        break
    print(i)

print('Range')
for i in r1:
    if i >= 100:
        break
    print(i)






