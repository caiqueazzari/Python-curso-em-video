#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

n = int(input('Digite um número: '))
print(f'A tabuada do número {n} é: \n')
x = 0

for x in range(11):
    print(f'{n} x {x} = {n * x}')
    x + 1

