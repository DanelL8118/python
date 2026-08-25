a = float(input('\ndigite o comprimento do lado A: '))
b = float(input('\ndigite o comprimento do lado B: '))
c = float(input('\ndigite o comprimento do lado C: '))

if a+b > c and a+c > b and b+c > a :
    
    print('\n{}\nAs medidas A({}), B({}) e C({}) podem formar um triangulo!\n{}\n'.format('=-'*20, a, b, c, '=-'*20))
    
    if a == b and a == c and b == c:
    
        print('triângulo equilátero\n')

    if a == b and a != c or b == c and b != a or a == c and a != b :
        
        print('triângulo isósceles\n')

    if a != b and a != c and b != c : 
        
        print('triangulo escaleno')

    
else :
    
     print('\n{}\nAs medidas A({}), B({}) e C({}) não podem formar um triangulo!\n{}\n'.format('=-'*20, a, b, c, '=-'*20))