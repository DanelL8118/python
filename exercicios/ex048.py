soma = 0; cont = 0

for c in range(1, 501, 2) :
    print(c)
    if c % 3 == 0 :
        soma += c
        cont += 1
print('soma dos {} valores = {}'.format(cont, soma))