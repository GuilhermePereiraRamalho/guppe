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
"""
# Desepacotamento de tupla
tupla = ('Geek University', 'Programação em Python: Essencial')
escola, curso = tupla

# 17:42
