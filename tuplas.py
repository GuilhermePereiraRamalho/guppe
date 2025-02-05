"""
Tuplas (tuple)

Tuplas são bastante parecidas com listas.

Existem duas diferenças básicas:
1 - A tuplas são representadas por parênteses ()
2 - As tuplas são imutáveis: Isso significa que ao se criar uma tupla ela não muda. Toda operação em uma tupla, gera uma nova tupla

# Cuidado 1: as tuplas são representadas por (), mas veja:
tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)

print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)

print(type(tupla2))

# Cuidado 2: Tuplas com 1 elemento
tupla3 = (4) # Isso não é uma tupla
print(tupla3)

print(type(tupla3))

tupla4 = (4,) # Isso é uma tupla
print(tupla4)

print(type(tupla4))

# Podemos concluir que tuplas são definidas pela virgula e não pelo uso dos parênteses

tupla5 = 4, # Isso é uma tupla
print(tupla5)

print(type(tupla5))

# Podemos gerar uma tupla dinamicamente com range(inicio, fim, passo)
tupla = tuple(range(11))
print(tupla)
print(type(tupla))

# Desepacotamento de tupla
tupla = ('Geek University', 'Programação em Python: Essencial')
escola, curso = tupla

print(escola)
print(curso)
# OBS: Gera erro ValueError se colocarmos um número diferente de elementos para desempacotar

# Métodos para adição e remoção não existem, uma vez que tuplas são imutaveis

# Soma*, Valor máximo*, Valor mínimo* e Tamanho funcionam em tuplas
# * Se os valores forem todos inteiros ou reais
tupla1 = (1, 2, 3, 4, 5, 6)

print(sum(tupla1))
print(max(tupla1))
print(min(tupla1))
print(len(tupla1))

# Concatenação de tuplas
tupla1 = (1, 2, 3)
print(tupla1)

tupla2 = (4, 5, 6)
print(tupla2)

print(tupla1+tupla2) #Tuplas são imutáveis

print(tupla1)
print(tupla2)

tupla3 = tupla1 + tupla2
print(tupla3)


tupla1 = tupla1 + tupla2 # Tuplas são imutáveis mas podemos sobrescrever seus valores
print(tupla1)

# Verificar se determinado elemento está contido na tupla
tupla = (1, 2, 3)

print(3 in tupla)
print(33 in tupla)

# Iterando sobre uma tupla
tupla = (1, 2, 3)

for n in tupla:
    print(n)

for i, v in enumerate(tupla):
    print(i, v)

# Contando elementos dentro de uma tupla
tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b')
print(tupla.count('d'))

escola = tuple('Geek University')
print(escola)

print(escola.count('e'))

# Dicas na utilização de tuplas

# Devemos utilizar tuplas sempre que não precisarmos modificar os dados contidos em uma coleção
# Exemplo 1
meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
print(meses)

# O acesso a elementos de uma tupla também é semelhante a de uma lista
print(meses[5])

# Iterar com while
i = 0

while i < len(meses):
    print(meses[i])
    i += 1

# Verificando em qual índice um elemento está na lista
meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
print(meses.index('Junho'))
# OBS: Caso o elemento não exista, será gerado ValueError

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

# Slicing
# tupla[inicio:fim:passo]
print(meses[5:9])

Por que utilizar tuplas?
 - Tuplas são mais rapidas do que listas.
 - Tuplas deixam seu código mais seguro*.
* Isso porque trabalhar com elementos imutáveis traz segurança para o código
"""
# Copiando uma tupla para outra
tupla = (1, 2, 3)

nova = tupla # Na tupla não temos o problema de shallow copy

print(nova)
print(tupla)

outra = (4, 5, 6)

nova = nova + outra

print(nova)
print(tupla)
