lista = []

def media_lista(lista):
    return sum(lista)/len(lista)

for i in range(5):
    n = float(input('Digite um número: '))
    lista.append(n)

print(f'A média desses números é {media_lista(lista):.2f}')
