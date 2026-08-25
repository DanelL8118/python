import math

ang = float(input('\ndigite o valor do angulo que deseja: \n'))

rad = math.radians(ang)

print('{} \npara o ângulo {:.2f}, temos: \nSENO: {:.2f}\nCOSSENO: {:.2f}\nTANGENTE: {:.2f} \n{}'.format('='*20, ang, math.sin(rad), math.cos(rad), math.tan(rad), '='*20))
