notas = []

for i in range(1, 5):
    nota = float(input(f'Insira a {i}ª nota: '))
    notas.append(nota)

media = sum(notas) / 4
print(f'A média dessas notas é {media:.2f}')