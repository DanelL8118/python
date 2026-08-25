real = float(input('\ndigite quandos reais você tem:(R$)'))

dolar = real / 3.27

print('\n{}\nCom R${:.2f} real(is), você pode comprar U${:.2f} dólar(es)\n{}\n'.format('='*20, real, dolar, '='*20))