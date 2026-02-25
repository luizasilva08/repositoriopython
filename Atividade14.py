def validar():
    while True:
        try:
            n = int(input('Insira um número inteiro: '))
            print(f'Seu número é {n}')
            break
        except ValueError:
            print('Digite um número inteiro!')
validar()