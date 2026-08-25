nome = input('digite seu nome: ').strip()

print('{}'.format(nome.upper()))
print('{}'.format(nome.lower()))
print('{}'.format(len(nome)-nome.count(' ')))
#print('{}'.format(nome.find(' ')))

separa = nome.split()

print('{}, {}'.format(separa[0], len(separa[0])))