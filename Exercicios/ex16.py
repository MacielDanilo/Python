# co = float(input('comprimento do Cateto oposto: '))
# ca = float(input('comprimento do Cateto Adjacente: '))
# hi = (co ** 2 + ca ** 2) ** (1/2)
# print('A medida da Hipotenusa é {:.2f}'.format(hi))

import math

co = float(input('comprimento do Cateto oposto: '))
ca = float(input('comprimento do Cateto Adjacente: '))
hi = math.hypot(ca, co)
print('A medida da Hipotenusa é {:.2f}'.format(hi))