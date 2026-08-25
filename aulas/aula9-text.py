frase = 'curso em video python'

print(frase[9])

print(frase[9:21])

print(frase[9:21:2])

print(frase[:5])

print(frase[15:])

print(frase[9::3])

len(frase)
#conta quantos cacacteres

frase.count('o')
frase.count('o', 0, 13)
#encontra caracteres

frase.find('deo')
frase.find('Android')
#fala a posição, se não exisitir retorna -1

'curso' in frase
#apenas encontra o trecho

frase.replace('python', 'android')

frase.upper()
#deixa tudo maiusculo
frase.lower()
#tudo minusculo

frase.title()
#deixa as primeiras letras maiusculas

frase.strip()
#remove espaços antes e depois da string
frase.rstrip()
#remove somente o ultimo espaço

frase.split()
#divide o string em vários, baseado em espaços

'-'.join(frase)
#coloca o caracter nos espaços da string