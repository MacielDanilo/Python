print('Conversão de Real para Dólar')
r = float(input('digite seu valor em real: R$'))
d = r / 5.14
print('Com R${:.2f}, você pode comprar US${:.2f}'.format(r, d))
