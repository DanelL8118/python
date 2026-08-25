from math import floor

num = float(input('\ndigite um número real: '))

print('\n{}\na parte inteira do número {} é: {}\n{}\n'.format('='*20, num, floor(num), '='*20))

#também poderia ser usado o trunc