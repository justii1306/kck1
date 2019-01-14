v = 13
print(v)
for i in range(15):
    print(i)
for i in range(4,15):
    print(i)
    if i == 14:
        print('Koniec')

def kwadrat(x):
    return x*x

lista = range(1, 15)
l = list(map(kwadrat, lista))
print(l)

lista = range(1, 15)
l = list(map(lambda x: x*x, lista))
print(l)
    
