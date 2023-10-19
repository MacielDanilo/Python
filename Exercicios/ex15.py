#mostrando um numero real em sua porção inteira

import math
# forma simples de resolver 
# num = float(input('Digite um numero: '))
# print('O numero Real {}, lido inteiro é: {}'.format(num, int (num)))

num = float(input('Digite um numero: '))
print('O numero Real {}, lido inteiro é: {:.0f}'.format(num, math.trunc(num)))