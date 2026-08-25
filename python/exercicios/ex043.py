peso = float(input('digite seu peso:(KG) '))

altura = float(input('digite sua altura:(M) '))

imc = peso / (altura ** 2)
status = str



if imc < 18.5 : status = 'abaixo do peso'

elif imc < 25 : status = 'peso ideal'

elif imc < 30 : status = 'sobrepeso'

elif imc < 40 : status = 'obesidade'

elif imc >= 40 : status = 'obsedidade mórbida'

print('\n{}\nAltura: {:.2f} m\nPeso: {:.2f} kg\nimc: {:.2f}\nDiagnóstico: {}\n{}\n'.format('=-'*20, altura, peso, imc, status, '=-'*20))

