"""
Tipo Booleano

Álgebra Booleana, criada por George Boole

2 constantes, Verdadeiro ou Falso

True - Verdadeiro
False - Falso

OBS: Sempre com a inicial maiúscula

Errado: true, false
Certo: True, False
"""

ativo = False

print(ativo)

"""
Operações básicas:
"""

# Negação(not)
"""
Fazendo a negação, se o valor booleano for verdadeiro o resultado será falso, se for falso o resultado será verdadeiro. Ou seja, sempre o contrário.
"""
print(not ativo)

logado = False
# Ou (or):
"""
É uma operação binária, ou seja, depende de dois valores. Ou um outro deve ser verdadeiro

True or True - True
True or False - True
False or True - True
False or False - False
"""
print(ativo or logado)

# E (and)
"""
Também é uma operação binária, ou seja, depende de dois valores. Ambos os resultados devem ser verdadeiro.
True or True - True
True or False - False
False or True - False
False or False - False
"""
