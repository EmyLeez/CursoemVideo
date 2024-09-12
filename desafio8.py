'''Leia o peso e altura de uma pessoa e mostre seu IMC
Abaixo de 18.5:Abaixo do peso
Entre 18.5 e 25: Peso ideal
25 até 30: Sobrepeso
30 até 40: Obesidade
Acima de 40: Obesidade mórbida'''

nome = str(input("Digite seu nome: "))
altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso em Kg: "))
imc = peso / (altura ** 2)

print("{} o seu IMC é {:.1f}".format(nome,imc))

if imc < 18.5:
    print("Abaixo do peso")

elif imc >= 18.5 or imc <= 25:
    print(" Peso ideal")

elif imc >=25 or imc <30:
    print("Sobrepeso")