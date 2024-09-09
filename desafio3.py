'''Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
0 primeiro valor é maior
0 segundo valor é maior
Não existe valor maior, os dois são iguais
'''
n1 = int(input("Digite seu n1: "))
n2 = int(input("Digite seu n2: "))

if n1 > n2:
    print(f" O Valor {n1} é maior")
elif n2 > n1:  
    print(f" O Valor {n2} é maior")
elif n1 == n2:  #ELSE também serviria por não ter uma terceira condição
    print("Não existe valor maior, os dois são iguais")
