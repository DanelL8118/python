salario = float(input('digite seu sálario: '))

if salario <= 1250 :
    
    total = salario * 1.15
    ali = 15

else : 
    
    total = salario * 1.10
    ali = 10

print('\n{}\nSalário atual: R$ {:.2f}\nSalário novo: R$ {:.2f}\nPorcentagem de aumento: {} %\n{}\n'.format('=-'*20, salario, total, ali, '=-'*20))