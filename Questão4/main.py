# -*- coding: latin1 -*-

def teste_numero_primo(num):
    n = int(num)
    mult = 0

    for count in range(2,n):
        if (n % count == 0):
            mult += 1
    if(mult == 0):
        return 1
    else:
        return 0

x = int(input('Digite um n�mero: '))
if teste_numero_primo(x) == 1:
    print('o n�mero ',x,' � primo.')
else:
    print('o n�mero ',x,' n�o � primo.')