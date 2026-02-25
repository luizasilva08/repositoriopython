lista = []
print('Escreva 5 números')
for i in range(5):
    n = float(input('Digite um número: '))
    lista.append(n)
print(f'A soma total da lista é {sum(lista)}')