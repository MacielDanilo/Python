nome = input('Qual é o seu Nome? ')

#print('Olá',nome, 'Prazer em te conhecer!')
print('Olá {} ! Prazer em te conhecer!'.format(nome))

dia = input('Qual o dia do seu nascimento? ')
mes = input('E qual o mes? ')
ano = input('Qual o ano? ')
print('Então Voce nasceu no dia',dia,'de',mes,'de',ano,'. Correto?')

print('Vamos fazer uma soma! ')
n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))
n3 = n1+n2

#print('A soma dos numeros',n1,'e',n2, 'é igual a {}'.format(n3))
print('A soma dos numeros {} e {} é igual a {}'.format(n1, n2, n3))


