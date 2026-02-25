def par_ou_impar(n):
    if (n%2==0):
        return "Par"
    else:
        return "Ímpar"
    
n=int(input('Escreva um numero e veja se é par ou ímpar: '))
print(par_ou_impar(n))