'''soma = 0
numero = int(input('digite: '))
while numero > 0:
    soma+= numero
    if soma >= 100:
        soma = 0
    numero = int(input('digite: '))

print(soma)    '''


numero = int(input('digite: '))
qtd = 1
while abs(numero) >= 10:
    numero = numero / 10
    qtd+= 1


print(qtd)  