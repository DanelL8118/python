n1 = float(input('\ndigite um número: '))

n2 = float(input('\ndigite um número: '))

n3 = float(input('\ndigite um número: '))

menor = n1

if n2 < n1 and n2 < n3: menor = n2

if n3 < n1 and n3 < n2: menor = n3

maior = n1

if n2 > n1 and n2 > n3: maior = n2

if n3 > n1 and n3 > n2: maior = n3

print('-=-'*20)

print('\nvalores digitados: {:.0f}, {:.0f}, {:.0f}\nMaior valor: {:.0f}\nMenor valor: {:.0f}\n'.format(n1, n2, n3, maior, menor))

print('-=-'*20)