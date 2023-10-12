dia = int(input('Quantos dias com o carro alugado? '))
km = float(input('Quantos KM rodados? '))
valord = dia * 60
valorkm = km * 0.15
total = valord + valorkm
#posso usar apenas uma variavel, exemplo: 
# total = (dia * 60) + (km * 0.15)
print('Voce deve pagar R${:.2f}'.format(total))