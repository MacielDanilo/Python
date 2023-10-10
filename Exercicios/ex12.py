sal = float(input('Qual é o salario do Funcionário? R$'))
novo = sal + (sal * 15 / 100)
print('Um funcionário recebia um salário de R${:.2f}, com o aumento de 15% passou a receber R${:.2f}'.format(sal, novo))