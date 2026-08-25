idade = int(input('\ndigite sua idade: '))

categoria = str

if idade <= 9 : categoria = 'mirim'

elif idade <= 14 : categoria = 'infantil'

elif idade <= 19 : categoria = 'junior'

elif idade <= 25 : categoria = 'sênior'

elif idade > 25 : categoria = 'master'

print('\n{}\nCom {} anos, você está na categoria {}\n{}\n'.format('=-'*20, idade, categoria, '=-'*20))
