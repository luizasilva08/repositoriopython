lista = []
sit =''

def adicionar():
    try:
        num = float(input('Adicione um número na lista: '))
        lista.append(num)
        print('\n\033[032mNúmero adicionado!\033[m')
        return lista
    except ValueError:
        print('\n\033[031mDigite em algarismos!\033[m')

def mostrar(lista):
    print(f'\033[033m\nSua lista: {lista}\033[m')

def media(lista):
    if len(lista)>0:
        media = sum(lista) / len(lista)
        print(f'\033[031m\nA média da sua lista é {media}\033[m')
    else:
        print('\n\033[031mDivisão por zero!\033[m')

def menu(sit):
    print('\n-----Menu------')
    sit = input('Digite: \n1 - Adicionar número na lista \n2 - Mostrar lista \n3 - Calcular média\n4 - Sair \n')

    if sit =='1':
        adicionar()
        menu(sit)
    elif sit =='2':
        mostrar(lista)
        menu(sit)
    elif sit =='3':
        media(lista)
        menu(sit)
    elif sit =='4':
        print('\033[036mVocê saiu.\033[m')
        exit()
    else:
        print('\033[034mOperação não encontrada.\033[m')
        menu(sit)

menu(sit)



#alteraçãooo0
