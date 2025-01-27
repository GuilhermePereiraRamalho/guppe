"""
Faça um programa que receba dois números inteiros e mostre qual deles é o maior.
"""


x: int = int(input("Digite o primeiro inteiro: "))
y: int = int(input("Digite o segundo inteiro: "))

if x > y:
    print(f"O maior entre {x} e {y} é: {x}")
elif y > x:
    print(f"O maior entre {x} e {y} é: {y}")
else:
    print(f'{x} e {y} são iguais!')
