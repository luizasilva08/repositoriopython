lista = []

def adicionar():
    sit = 's'
    while sit == 's':
        produto = (input(f'Adicione um produto na sua lista de compras: '))
        lista.append(produto)
        sit = input('Você quer continuar? Se sim, digite "s": ')
        if sit =='s':
            continue
        else:
            break
    return lista

def remover(produto):
    print(lista)
    while True:
        produto = input('Você quer remover algum produto desta lista?\n Se sim, escreva esse produto: ')
        if produto in lista:
            lista.remove(produto)
            print(f'Sua lista de compras no momento: {lista}')
        else:
            print('Produto não encontrado ou operação recusada.')
            break

produtos = adicionar()
remover(produtos)

