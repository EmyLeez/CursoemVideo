nome = input('Digite seu nome minha cara: ')
print('Prazer em te conhecer {:=^20}!'.format(nome)) #Brincando com o python

n1 = int(input('Digite um  valor: '))
n2 = int(input('Digite um valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
sub = n1 - n2
di = n1 // n2
e = n1 ** n2

#Assim se for para mostrar na tela, para usar em outras coisas é bom criar a váriavel
print('A soma  de {} e {} é {}'.format(n1,n2,n1+n2))

print('A soma é {}, \n o produto é {} e a divisão é {:.3f}'.format(s,m,d),end=' ')
print('A Divisão inteira {} e potência {}'.format(di,e))


