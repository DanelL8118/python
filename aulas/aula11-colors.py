print('\033[1;31;43mOlá mundo\033[m')

#styles 0, 1 4, 7
#text 30 a 37
#back 40 a 47

#formato \033[style;text;backm
#dá pra usar no .format também

cores = {'limpa' : '\033[m', 
         'azul' : '\033[34m',
         'amarelo' : '\033[33m',
         'pretobranco' : '\033[7;30m'}

print('{}não sei oque não sei oque lá{}'.format(cores['azul'], cores['limpa']))

#se vira pra descobrir o resto

