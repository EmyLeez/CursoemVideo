'''Programa que leia o ano de nascimento e mostre a categoria de acordo com a idade:
Até 9 anos : Mirim
Até 14 anos: Infantil
Até 19 anos: Júnior
Até 25 anos: Senior
Acima:Master'''

#from datetime import date  quando quero fazer por funções
# atual = fate.today().year
nasc = int(input("Digite o ano de seu nascimento: "))
ano_atual = int(input("Digite o ano atual: "))
idade = ano_atual - nasc
print(f"O atleta tem {idade} anos")

if idade <= 9:
    print("Classificação: mirim")
    
#Poderia colocar só até 14 pois ele não seria maior de 9
elif idade >9 and idade <=14: 
    print("Classificação: Infantil")
elif idade <=19:
    print("Classificação: Júnior")
elif idade <=25:
     print("Classificação: Sênior")
else:
    print("Classificação: Master ")



