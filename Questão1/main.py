#!/usr/bin/env python
# -*- coding: latin 1 -*-
id = int(input('Digite sua idade em dias:'))

ia = int (id / 365) #onde ia é a idade em anos
im =int((id % 365) / 30) #onde im é a idade em meses
rd = (id % 365) % 30 #onde rd é dias restantes

print ('A idade em anos, meses e dias =', ia, 'anos', im, 'meses', rd, 'dias')
