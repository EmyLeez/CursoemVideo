#Faça um programa  que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ela.

surpresa = input("Digite qualquer coisa: ")

#O TIPO
print("O tipo primitivo da minha surpresa é",type(surpresa))

# SE TEM ESPAÇOS (NÃO LER ENTER)
print('Só tem espaços?', surpresa.isspace())

# SE TEM NÚMEROS
print('É um número?', surpresa.isnumeric())

# SE TEM LETRAS
print('É alfabético?', surpresa.isalpha())

# SE TEM NÚMEROS E LETRAS
print('É alfanúmerio?', surpresa.isalnum())

#SE ESTÁ EM MAIÚSCULAS
print('Está em maiúscula?', surpresa.isupper())

#SE ESTÁ EM MINÚSCULAS
print('Está em minúsculas?', surpresa.islower())
#print(surpresa.islower())

#VERIFICA SE ESTÁ Assim
print('Está capitalizada?', surpresa.istitle())

