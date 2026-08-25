frase = str(input('\ndigite uma frase: ')).upper().strip()

print('\n{}\nna frase {}\nExistem {} letras A\nAparece primeiro em {}\nAparece por último em {}\n{}'.format('='*20, frase, frase.count('A'), frase.find('A')+1, frase.rfind('A')+1, '='*20))