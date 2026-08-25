km = float(input('\ndigite os KM rodados: '))
dia = int(input('\ndigite quantos dias ele foi usado: '))

total = dia * 60 + km * 0.15

print('\n{}RESULTADO{}\n  valor a pagar:\n  R$ {:.2f}\n{}\n'.format('='*20, '='*20, total, '='*49))