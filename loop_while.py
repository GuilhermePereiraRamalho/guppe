"""
Loop while

Forma geral:

while expressão_booleana:
    //execução do loop

O bloco do while será repetido enquanto a expressão booleana for verdadeira.

Expressão booleana é toda expressão onde o resultado é verdadeiro ou falso
"""

# Exemplo 1
# numero = 1
#
# while numero < 10:
#     print(numero)
#     numero += 1
# OBS: Em um loop while, é importante que cuidemos do critério de parada para não causar um loop infinito

resposta = ''

while resposta != 'sim':
    resposta = input('Deseja parar? ')
