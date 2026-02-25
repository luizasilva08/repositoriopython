def ler():
    lista = []
    for i in range(1,4):
        nota = float(input(f'Digite sua {i}ª nota: '))
        lista.append(nota)
    return lista

def media(lista):
    return sum(lista) / len(lista)

def mostrar(lista, media):
    print(f'Suas notas: {lista}')
    print(f'Sua média é {media:.2f}')

notas = ler()
resultado = media(notas)
mostrar(notas, resultado)


