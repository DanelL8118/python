from datetime import date

ano = int(input('digite seu ano de nascimento: '))

anoAtual = date.today().year

idade = anoAtual - ano

faltam = abs(18 - idade)

if idade < 18 :

    print('\n{}\nQuem nasceu em {} tem {} anos em {}\nAinda faltam {} para seu alistamento\nSeu alistamento será no ano de {}\n{}\n'.format('=-'*20, ano, idade, anoAtual, faltam, anoAtual+faltam, '=-'*20))
    
elif idade > 18 :
    
     print('\n{}\nQuem nasceu em {} tem {} anos em {}\nDeveria ter se alistado há {} ano\nSeu alistamento foi no ano de {}\n{}\n'.format('=-'*20, ano, idade, anoAtual, faltam, anoAtual+faltam, '=-'*20))
     
else :
    
  print('\n{}\nQuem nasceu em {} tem {} anos em {}\nVai se alistar vagabundo\n{}\n'.format('=-'*20, ano, idade, anoAtual, '=-'*20))