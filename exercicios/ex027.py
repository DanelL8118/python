nome = str(input('\nDigite o seu nome: \n')).strip()

n = nome.split()

print('\n{}\nnome completo: {}\nprimeiro nome: {}\núltimo nome: {}\n{}'.format('='*20, nome, n[0], n[-1], '='*20))