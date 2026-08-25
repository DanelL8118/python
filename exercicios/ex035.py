a = float(input('\ndigite o comprimento do lado A: '))
b = float(input('\ndigite o comprimento do lado B: '))
c = float(input('\ndigite o comprimento do lado C: '))

if a+b > c and a+c > b and b+c > a :
    
    print('\n{}\nAs medidas A({}), B({}) e C({}) podem formar um triangulo!\n{}\n'.format('=-'*20, a, b, c, '=-'*20))
    
else :
    
     print('\n{}\nAs medidas A({}), B({}) e C({}) não podem formar um triangulo!\n{}\n'.format('=-'*20, a, b, c, '=-'*20))

