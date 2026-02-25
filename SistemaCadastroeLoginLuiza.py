usuario = 'admin'
senha = '123'

idade = 0
nome = ' '
salario = 0


print('\033[034mSistema de Cadastro\033[m')
print(f"{'=':=^30}")

def ler_nome(msg1):                                                 #Função para o nome
    while True:
        try:
            nome = str(input('Insira o seu nome completo: '))

            checkNum = any(Num.isdigit() for Num in nome)

            palavras = nome.strip().split()

            if len(palavras) >= 2:
                break

            elif (checkNum==True):
                print('Insira nome e sobrenome com letras.')

            else:
                print('Insira nome e sobrenome com letras e dividos por um espaço.')

        except:
            print('Insira seu nome completo com espaços.')

def ler_idade(msg2):                                                 #Função para idade
    while True:
        try:
            idade = int(input('Insira a sua idade: '))

            if idade<0:
                print('Escreva um número inteiro não negativo.')

            elif idade<18 or idade>100: 
                print('Menor de idade ou idade inválida.')

            else: 
                break

        except ValueError:
            print('Escreva um número inteiro')
            
def ler_salario(msg3):                                             #Função para salario
    while True:
        try:
            salario = float(input('Insira o seu salário: '))

            if salario<=0:
                print('Salário não pode ser negativo ou zerado.')
            
            else:
                break

        except ValueError:
            print('Insira um número flutuante (ex: 12.0)')

nome = ler_nome(nome)
idade = ler_idade(idade)
salario = ler_salario(salario)


print(f"\n{'=':=^30}")
print('\033[031mSistema de Login\033[m')
print(f"{'=':=^30}")

while True:                                               #Sistema de Login
    try:
        usuario = str(input('Insira o usuário: '))
        if usuario == 'admin':
            senha = str(input('\nInsira a senha de acesso: '))
            try:
                if senha=='123':
                    print('\033[033mLogin liberado!\033[m')
                    break

                else: 
                    print('\031[033mSenha incorreta.\031[m \n\033[034mInsira o usuário novamente.\033[m')

            except ValueError:
                print('Insira números inteiros.')
        else:
            print('Usuário não encontrado.')

    except ValueError:
        print('Use letras, sem espaços.')



