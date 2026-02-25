lista = []

def qtd(lista):
    return len(lista)

while True:
    try:
        n = input('Digite um valor para colocar na lista: ')
        lista.append(n)
        print(f'Quantidade de itens na lista: {qtd(lista)}')

    except ValueError:
        print('Digite em algarismos.')