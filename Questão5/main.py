# -*- coding: latin1 -*-

def inversao_palavras(frase_normal):
   frase = str(frase_normal)
   invertida = ' ' .join(palavra[::-1] for palavra in frase.split())
   return invertida

print('frase invertida: ', inversao_palavras('O c�u � azul'))