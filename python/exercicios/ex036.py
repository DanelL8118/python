casa = float(input('\ndigite o valor da casa: \n'))
salario = float(input('digite o seu salário: R$ \n'))
anos = int(input('digite em quantos anos deseja pagar: \n'))

prestacao = casa / (anos*12)

if prestacao > salario*0.30 : 
    
    print('\nTu não consegue pagar paizao, foi mal\n{:.2f}\n'.format(prestacao))
    
else :
    
    print('\nTá de boa pae, pode comprar lá\n{:.2f}\n'.format(prestacao))
