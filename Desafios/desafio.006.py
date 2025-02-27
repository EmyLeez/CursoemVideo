#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = float(input('Digite um número: '))

dobro = n * 2
triplo = n * 3
raiz = n ** (1/2)
print('O número digitado é {}, \n seu dobro é {}, o triplo {} e a raiz quadrada é {:.2f}'.format(n,dobro,triplo,raiz))