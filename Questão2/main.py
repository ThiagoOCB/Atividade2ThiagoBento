# -*- coding: latin1 -*-

import math
print('Abaixo ser� solicitado os valores de a, b e c, \
onde a � o lado esquerdo de um tri�ngulo,\
 b � o lado direito e c � o lado de baixo')
a = int(input('Digite o valor de a:'))
b = int(input('Digite o valor de b:'))
c = int(input('Digite o valor de c:'))

if(a > b + c):
    print ('os valores ',a,', ', b,' e ',c, 'n�o formam um tri�ngulo.')
else:
    p = float((a + b + c) / 2)
    area = float(math.sqrt(p*(p-a)*(p-b)*(p-c)))
    print('�rea do tri�ngulo: ',area)