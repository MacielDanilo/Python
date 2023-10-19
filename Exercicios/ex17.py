import math
ang = float(input('Digite o angulo: '))
seno = math.sin(math.radians(ang))
coss = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))
print ('O Seno é {:.2f}\n O Cosseno é {:.2f}\n A Tangente é {:.2f}'.format(seno, coss, tang))