"""
Módulo Collections - Counter

Collections -> High-performance Container Datatypes

Counter -> Recebe um iteravel como parametro e cria um objeto do tipo Collections Counter que é parecido com um dicionadio contendo como chave o elemento da lista passada como parametro e como valor a quantidade de ocorrencias desse elemento.

# Exemplo 1
from collections import  Counter

# Podemos usar qualquer iteravel, aqui usamos uma lista
lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 5, 5, 5, 3, 45, 45, 66, 66, 43, 34]
# Utilizando o Counter
res = Counter(lista)

print(type(res))
print(res)

# Counter({1: 5, 3: 5, 5: 5, 2: 4, 4: 2, 45: 2, 66: 2, 43: 1, 34: 1})
# Veja que, para cada elemento da lista, o Counter criou uma cheve e colocou como valor a quantidade de ocorrencias

# Exemplo 2
from collections import  Counter

print(Counter("Geek University"))
# Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})
"""
# Exemplo 3
from collections import  Counter

texto = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce laoreet quam et pulvinar feugiat. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Curabitur sed maximus enim. Suspendisse non magna elit. Integer ultrices rutrum lacus, eu accumsan tellus scelerisque et. Aliquam placerat convallis tristique. Curabitur convallis massa nunc, ut tempor dolor mollis id. Quisque odio leo, condimentum nec erat et, pharetra tristique odio. Suspendisse potenti. Vestibulum ac urna nibh. Phasellus eu auctor nisl, eu volutpat neque. Cras viverra arcu eu purus accumsan, non fringilla arcu ullamcorper. Sed blandit, nisl eget ornare commodo, massa dolor facilisis ante, id pharetra ante neque at lectus. Morbi ac urna a erat fringilla porttitor et in eros. In feugiat, ligula eget congue ullamcorper, eros ipsum condimentum nulla, nec lacinia leo sem consequat tellus. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.
"""

palavras = texto.split()

# print(palavras)

res = Counter(palavras)
print(res)

# Encontrando as 5 palavras com mais ocorrencias no texto
print(res.most_common(5))
