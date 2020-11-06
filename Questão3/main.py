# -*- coding: latin1 -*-

a = int(input('Digite o primeiro número:'))
b = int(input('Digite o segundo número:'))
c = int(input('Digite o terceiro número:'))

if (a < b) and (a < c):
    print('O número ', a, ' é o menor número digitado')
elif (b < a) and (b < c):
    print('O número ', b, ' é o menor número digitado')
else:
    print('O número ', c, ' é o menor número digitado')