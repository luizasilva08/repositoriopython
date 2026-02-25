lista = []
pares = []

def filtrar_pares(numeros):                #insere os números em uma lista 'pares'
    for i in numeros:
        if (i%2==0):
            pares.append(i)
    return pares

print('Escreva 6 números')
for i in range(6):
    n = float(input('Digite um número: '))
    lista.append(n)

print(lista)
print('Os numeros pares desta lista são:', filtrar_pares(lista))