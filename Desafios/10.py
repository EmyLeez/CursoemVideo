# Programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
# 1 dolar = 5.70


valor = float(input('Quanto R$ você tem hoje em sua carteira? R$ '))

convertendo =  valor  / 5.70


print( 'O valor em R$ é {:.2f} e convertendo você tem US${:.2f}'.format (valor,convertendo))