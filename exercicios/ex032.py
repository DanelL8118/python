from datetime import date

ano = int(input('\ndigite o ano: \n'))

print('-=-'*20)

if ano == 0: 
    
    ano = date.today().year
    
if ano%4 == 0 and ano%100 != 0 or ano%400 == 0: print('\nO ano de {} é bissexto\n'.format(ano))

else: print('\nO ano de {} não é bissexto\n'.format(ano))

print('-=-'*20)