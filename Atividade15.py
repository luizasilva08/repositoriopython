lista = []

def somar(lista):
    return sum(lista)

while True:
    try:
        n = float(input('Digite um número para colocar na lista: '))
        lista.append(n)
        print(f'Soma dos números na lista: {somar(lista)}')

    except ValueError:
        print('Digite em algarismos.')