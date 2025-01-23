"""
3. Faça um programa que recebe três valores e apresente a soma dos quadrados dos valores lidos.
"""
from time import  sleep

print('Olá, vou precisar que você me informe três números inteiros')
sleep(1)

n1: int = int(input("Informe o primeiro número: "))
n2: int = int(input("Informe o segundo número: "))
n3: int = int(input("Informe o terceiro número: "))

soma_dos_quadrados: int = n1**2 + n2**2 + n3**2

print(f'Os números digitados foram: {n1}, {n2}, {n3}')
print(f'A soma dos quadrados dos valores é: {soma_dos_quadrados}')
