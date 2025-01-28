"""
Loop for
Loop -> Estrutura de repetição

C ou Java
for(int i; i<10; i++){
    //execução do loop
}

Python
for item in interavel:
    //execução do loop

Utilizamos loops para iterar sobre sequências ou sobre valores iteraveis

Exemplos de iteraveis:
 - String
 - Lista
 - Range

 for _, v in enumerate(nome):
    print(v)
OBS:  quando nao precisamos de um valor, podemos descarta-lo utilizando um underline
"""

nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)

# Exemplo de for 1 (Iterando em uma string)
# for letra in nome:
#     print(letra)

# Exemplo de for 2 (Iterando em uma lista)
# for numero in lista:
#     print(numero)

# Exemplo de for 3 (Iterando sobre um range)
# for numero in range(1, 10):
#     print(numero)

# for i, v in enumerate(nome):
#     # print(nome[i])
#     print(v)

# for valor in enumerate(nome):
#     print(valor)
#     print(valor[0])
#     print(valor[1])

# qtd = int(input('Quantas vezes esse loop deve rodar? '))
# soma = 0
#
# for n in range(1, qtd+1):
#     num = int(input(f'Informe o {n}/{qtd} valor: '))
#     soma += num
# print(f'A soma é {soma}')

# for letra in nome:
#     print(letra, end="")

# original : U+1F605
# modificado: U0001F605

for _ in range(3):
    for numero in range(1, 11):
        print('\U0001F605' * numero)
