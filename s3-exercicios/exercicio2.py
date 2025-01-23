"""
2. Faça um programa que peça para o usuário digitar três valores inteiro e imprima a soma deles.
"""
from time import  sleep


print('Olá, vou precisar que você me informe três números inteiros')
sleep(1)

n1: int = int(input("Informe o primeiro número: "))
n2: int = int(input("Informe o segundo número: "))
n3: int = int(input("Informe o terceiro número: "))

soma: int = n1 + n2 + n3

print(f'Os números digitados foram: {n1}, {n2}, {n3}')
print(f'A soma deles é: {soma}')
