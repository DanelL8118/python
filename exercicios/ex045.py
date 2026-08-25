from random import randint

escolha = int(input('\n[ 0 ] Pedra\n[ 1 ] Papel\n[ 2 ] Tesoura \n\nDigite sua escolha: '))

itens = ('PEDRA', 'PAPEL', 'TESOURA')

computer = randint(0,2)

print('\nUsuário escolheu: {}\nComputador escolheu: {}\n'.format(itens[escolha], itens[computer]))

print('=-'*20)


if computer == 0 : #PEDRA
    if escolha == 0:
        print('\nEMPATE\n')
    elif escolha == 1:
        print('\nUSUARIO GANHOU\n')
    elif escolha == 2:
        print('\nCOMPUTADOR GANHOU\n')
    else : 
        print('\nopção inválida!\n')
    
elif computer == 1 : #PAPEL
    if escolha == 0:
        print('\nCOMPUTADOR GANHOU\n')
    elif escolha == 1:
        print('\nEMPATE\n')
    elif escolha == 2:
        print('\nUSUARIO GANHOU\n')
    else : 
        print('\nopção inválida!\n')
    
elif computer == 2 : #TESOURA
    if escolha == 0:
        print('\nUSUARIO GANHOU\n')
    elif escolha == 1:
        print('\nCOMPUTADOR GANHOU\n')
    elif escolha == 2:
        print('\nEMPATE\n')
    else : 
        print('\nopção inválida!\n')
        
print('=-'*20)
