'''Faça um programa que leia o ano de um nascimento de um jovem e informe, de acordo com sua idade:
Se ele ainda vai se alistar ao serviço militar (mostrar o tempo que falta)
Se é a hora de se alistar
Se já passou do alistamento (mostrar o tempo que passou)'''
#Colocar sexo feminino e masculo, se feminino não faz nada, masculino processa tudo

ano = int(input("Digite o ano que você nasceu: "))
ano_atual = int(input("Digite o ano atual: "))
# Ao contrário fica negativo pois o ano que estamos é maior.
idade =  ano_atual - ano 
print(f"Quem nasceu em {ano} tem {idade} anos em {ano_atual}")
if idade == 18:    
    
    print(f" Você tem  {idade} e pode se alistar ")

elif idade >18:
    tempo =  idade - 18
    print(f"Já passou {tempo} anos")  
    alistamento = ano_atual - tempo # Para saber quanto tempo passou
    print(f"Seu alistamento foi em {alistamento}") 

elif idade <18:
    tempo = 18 - idade # Cálculo para saber o tempo
    print(f"Faltam {tempo} anos para se alistar")
    alistamento = ano_atual + tempo #Para saber quando será
    print(f"Seu alistamento será em {alistamento}") 
