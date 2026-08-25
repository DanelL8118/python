import math

a = float(input('\ndigite o comprimento do cateto adjacente: '))

b = float(input('\ndigite o comprimento do cateto oposto: '))

#h = math.sqrt(pow(a, 2) + pow(b, 2))
h = math.hypot(a, b)

print('\n{}\ncateto adjacente: {:.2f}\ncateto oposto: {:.2f}\nhipotenusa: {:.2f}\n{}\n'.format('='*20, a, b, h, '='*20))