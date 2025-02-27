#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1 + n2) / 2

print('Suas notas são {:.1f} e {:.1f} e sua média é {:.1f}'.format(n1,n2,media))