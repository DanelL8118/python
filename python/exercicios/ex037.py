
numero = int(input('\ndigite o número que deseja converter: '))

tipo = int(input('\n[ 1 ] binário\n[ 2 ] octal\n[ 3 ] hexadécimal\n\nEscolha um dos tipos: '))

if tipo == 1 : 
    
    resultado = bin(numero)

elif tipo == 2 : 
    
    resultado = oct(numero)
    
elif tipo == 3 :
    
    resultado = hex(numero)
    
else : print('nenhuma opção escolhida!')
    
print('\n{}\nNúmero {} convertido em {}\n{}\n'.format('=-'*20, numero, resultado[2:], "=-"*20))