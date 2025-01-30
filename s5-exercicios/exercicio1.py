"""
1. Faça um programa que determine e mostre os cinco primeiros múltiplos de 3, considerando números maiores que 0.
"""

count: int = 0
i = 1

while count < 5:
    if i % 3 == 0:
        print(i)
        count += 1
    i += 1
