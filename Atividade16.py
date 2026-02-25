lista = []

def maior(lista):
    return max(lista)

while True:
    try:
        n = float(input('Digite um número para colocar na lista: '))
        lista.append(n)
        print(f'Maior número na lista: {maior(lista)}')

    except ValueError:
        print('Digite em algarismos.')