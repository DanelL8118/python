preco = float(input('\n========LOJA========\ndigite o preço do produto:\nR$ '))

opc = int(input('\n[ 1 ] à vista (10% off)\n[ 2 ] à vista no cartão (05% off)\n[ 3 ] em até 2x no cartão\n[ 4 ] em 3x ou mais no cartão (20% de juros)\n\nDigite a opção de pagamento: '))

if opc == 1 : total = preco * 0.90

elif opc == 2 : total = preco * 0.95

elif opc == 3 : total = preco

elif opc == 4 : total = preco * 1.20

else : total = preco

print('\n{}\nPreço normal: R$ {:.2f}\nOpção de pagamento escolhida: {:.0f}\nTotal a pagar: R$ {:.2f}\n{}'.format('=-' * 20, preco, opc, total, '=-' * 20))