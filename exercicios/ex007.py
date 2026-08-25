nome = input('digite o nome do aluno: ')
nota1 = float(input('digite a nota: '))
nota2 = float(input('digite a nota: '))

print('\nmédia do aluno {}: \nnotas {:.2f} e {:.2f} é igual a: {:.2f}'.format(nome, nota1, nota2, (nota1+nota2)/2))
