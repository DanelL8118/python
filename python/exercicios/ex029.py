km = int(input('\ndigite quantos km/h seu carro está: '))

print('-=-'*20)

if km <= 80:
    print('\nestá dentro dos limites, parabéns!\n')
else:
    
    multa = (km-80) * 7

    print('\nFora dos limeites de velocidade! 80 km/h\nMulta a pagar: R$ {:.2f}\n'.format(multa))
    
print('-=-'*20)