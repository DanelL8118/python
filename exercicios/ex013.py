nome = input('\ndigite o nome do funcionário\n')
sal = float(input('\ndigite o sálario do funcionário: R$ '))

print(f'='*20)
print('\nfuncionário: {}'.format(nome))
print('salário anterior: R$ {:.2f}\nnovo salário: R$ {:.2f}\n'.format(sal, sal + sal*15/100))
print(f'='*20)
