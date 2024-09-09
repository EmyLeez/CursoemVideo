'''36 ° Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa.O programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar. 
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou entao o emprestiumo sera negado.
'''
casa = float(input("Digite o valor da casa: R$ "))
salario_comprador = float(input("Digite seu sálario: R$ "))
anos_pagamento = int(input("Digite os anos em que você vai pagar: "))
parcela = casa/(anos_pagamento*12) #Multiplicado para saber quantos anos
minimo = salario_comprador * 30 /100 # Para tirar a porcentagem devemos multiplicar o valor que queremos e depois dividir por 100

print("Para pagar uma casa de R$ {:.2f} em {} anos, a prestação será de R$  {:.2f}" .format(casa, anos_pagamento, parcela))

if parcela <= minimo:
    print("Emprestimo negado")
else:
    print("Emprestimo aprovado")