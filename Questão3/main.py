# -*- coding: latin1 -*-

a = int(input('Digite o primeiro n�mero:'))
b = int(input('Digite o segundo n�mero:'))
c = int(input('Digite o terceiro n�mero:'))

if (a < b) and (a < c):
    print('O n�mero ', a, ' � o menor n�mero digitado')
elif (b < a) and (b < c):
    print('O n�mero ', b, ' � o menor n�mero digitado')
else:
    print('O n�mero ', c, ' � o menor n�mero digitado')