# -*- coding: latin1 -*-

import math
print('Abaixo será solicitado os valores de a, b e c, \
onde a é o lado esquerdo de um triângulo,\
 b é o lado direito e c é o lado de baixo')
a = int(input('Digite o valor de a:'))
b = int(input('Digite o valor de b:'))
c = int(input('Digite o valor de c:'))

if(a > b + c):
    print ('os valores ',a,', ', b,' e ',c, 'não formam um triângulo.')
else:
    p = float((a + b + c) / 2)
    area = float(math.sqrt(p*(p-a)*(p-b)*(p-c)))
    print('Área do triângulo: ',area)