from random import randint

min_number = int(input('Por favor, digite um numero minimo: '))
max_number = int(input('Por favor, digite um numero maximo: '))

if (max_number < min_number):
    print('Valor de entrada invalido - Desligando...')
else:
    rnd_number = randint(min_number, max_number)
    print(rnd_number)
