l = float(input('Largura da Parede:'))
a = float(input('Altura da Parede:'))
area = l * a
tinta = area / 2 
# tinta = area * (1/2) 
print('Sua parede tem as dimensoes {}x{} e sua área é de {}m².'.format(l, a, area))
print('Para pintar essa parede você precisará de {:.3f}l de tinta.'.format(tinta))