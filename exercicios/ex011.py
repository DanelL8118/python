l = float(input('\ndigite a largura da parede: (m) '))
a = float(input('\ndigite a altura da parede: (m) '))

m2 = l * a

print('\n{}\npara pintar a parede de {:.2f} m², será necessário {:.2f} Litros de tinta\n{}\n'.format('='*20, m2, m2/2, '='*20))
