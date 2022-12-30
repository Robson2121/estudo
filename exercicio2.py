v = int(input('Digite o valor para o saque:'))

print(f'Para o valor {v} são necessarias {int(v//100)} notas de 100')
re1 = v%100

print(f'Para o valor {v} são necessaria {int(re1//50)} notas de 50')

re2 = re1 % 50

print(f'Para o valor {v} são necessária {int(re2//10)} notas de 10')

re3 = re2 % 10

print(f'Para o valor {v} são necessária {int(re3//1)} notas de 1')
