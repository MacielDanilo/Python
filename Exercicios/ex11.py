prod = float(input('Digite o preço do produto: R$'))
desc = prod - (prod * 5 / 100)
print('O Produto que custava R${:.2f}, com o desconto de 5% passou a custar R${:.2f}'.format(prod, desc))
