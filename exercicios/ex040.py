n1 = float(input('digite a sua nota N1: '))

n2 = float(input('digite a sua nota N2: '))

media = (n1 + n2) / 2

if media >= 7.00 : print('\n{}\nVocê está aprovado com a média {}\n{}\n'.format('=-'*20, media, '=-'*20))
    
elif media < 5.00 : print('\n{}\nVocê está reprovado com a média {}\n{}\n'.format('=-'*20, media, '=-'*20))
    
elif media >= 5.00 and media < 7.00 : print('\n{}\nVocê está de recuperação com a média {}\n{}\n'.format('=-'*20, media, '=-'*20))