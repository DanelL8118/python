preço = float(input('\ndigite o valor do produto: R$ '))

total = preço * 0.95

print('\n{}\ntotal a pagar: (5% de desconto)\n  R$ {:.2f}\n{}\n'.format('='*20, total, '='*20))