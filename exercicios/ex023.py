num = int(input('\ndigite um número: \n'))

u = num // 1%10
d = num // 10%10
c = num // 100%10
m = num // 1000%10

print('{} {} {}'.format('='*20, num, '='*20))
print('\nmilhar: {}'. format(m))
print('\ncentena: {}'.format(c))
print('\ndezena: {}'.format(d))
print('\nunidade: {}'.format(u))
print('\n{} {} {}'.format('='*20, num, '='*20))