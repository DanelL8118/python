m = float(input('digite uma metragem: '))

print(f'\n{"="*5}RESULTADO{"="*5}\n' )
print('metros: {:.2f}\ncentímetros: {:.0f} \nmilímetros: {:.0f}\n'.format(m, m*100, m*1000))