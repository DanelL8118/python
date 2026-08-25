#import random
from random import choice

nome1 = input('\ndigite o nome do aluno: ')
nome2 = input('\ndigite o nome do aluno: ')
nome3 = input('\ndigite o nome do aluno: ')
nome4 = input('\ndigite o nome do aluno: ')

nomes = [nome1, nome2, nome3, nome4]

print('\n{} \naluno escolhido: {} \n{}'.format('='*20, choice(nomes), '='*20))