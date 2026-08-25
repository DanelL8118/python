from random import randint
from time import sleep

n = int(input('\ntente adivinhar meu número entre 0 e 5: '))

y = randint(0, 5)

print('\n===PENSANDO===\n')
sleep(3)

if n == y: 
    print('\nmeu número: {}\nseu número: {}\nVocê acertou, parabéns!\n'.format(y, n))
else:
    print('\nmeu número: {}\nseu número: {}\nVocê errou, parabéns!\n'.format(y, n))
