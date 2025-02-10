"""
Conjuntos

- Conjuntos em qualquer linguagem de programação, estamo fazendo referência à Teoria dos Conjuntos da Matemática.

- Em Pyhton os conjuntos são chamados de Sets.

Dito isso, da mesma forma que na matemátia:
- Sets(conjuntos) não possuem valores duplicados;
- Sets(conjuntos) não possuem valores ordenados;
- Elementos não são acessados via índica, ou seja, conjuntos não são indexados;

Conjuntos são bons para se utilizar quando precisamos armazenar elementos mas não nos importamos com a ordenação deles. Quando nao precisamos se preocupar com chaves, valores e itens duplicados.

Os conjuntos (sets) são referenciados em Python com chaves {}

Diferença entre Conjuntos(Set) e Mapas (Dicionario) em Python:
    - Um dicionário tem chave/valor;
    - Um conjunto tem apenas valor;

# Definindo um Conjunto:

# Forma 1
s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3}) # Repare que temos valores repetidos
print(s)
print(type(s))
# OBS: Ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo sera ignorado sem gerar error e não fará parte do conjunto

# Forma 2 - Mais comum
s = {1, 2, 3, 4, 5, 5}
print(s)
print(type(s))

# Podemos verificar se determinado elemento está contido no conjunto
if 3 in s:
    print('Tem o 3')
else:
    print('Não tem o 3')
"""
# Importante lembrar que além de não termos valores duplicados, não temos ordem

# Listas aceitam valores duplicados, então temos 10 elementos
lista = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
print(f'Lista: {lista} com {len(lista)} elementos')

# Tuplas aceitam valores duplicados, então temos 10 elementos
tupla = 99, 2, 34, 23, 2, 12, 1, 44, 5, 34
print(f'Tupla: {tupla} com {len(tupla)} elementos')

# Dicionarios não aceitam chaves duplicadas, então temos 8 elementos
dicionario = {}.fromkeys(lista, 'dict')
print(f'Dicionário: {dicionario} com {len(dicionario)} elementos')

# Conjuntos não aceitam valores duplicados, então temos 8 elementos
conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}
print(f"Conjunto: {conjunto} com {len(conjunto)} elementos")
