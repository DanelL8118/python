km = float(input('\ndigite a distância da viagem: '))

print('-=-'*20)

if km <= 200: print('\nvalor da viagem: R$ {:.2f}\n'.format(km*0.50))
    
else: print('\nvalor da viagem: R$ {:.2f}\n'.format(km*0.45))

print('-=-'*20)