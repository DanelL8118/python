n1 = int(input('digite o primeiro número: '))
n2 = int (input('digite o segundo número: '))

if n1 > n2 : print('\n{}\nO número {} é maior que o número {}\n{}\n'.format('=-'*20, n1, n2, '=-'*20))
    
elif n2 > n1 : print('\n{}\nO número {} é maior que o número {}\n{}\n'.format('=-'*20, n2, n1, '=-'*20))

elif n1 == n2 :     print('\n{}\nO número {} é igual ao número {}\n{}\n'.format('=-'*20, n1, n2, '=-'*20))