"""
Listas

Listas em Python funcionam como vetores/matrizes (arrays) em outras linguagens, com a diferença de serem DINÂMICO e também dde podermos colocar QUALQUER tipo de dado.

Linguagens C/JAVA: Arrays
    - Possuem tamanho e tipo de dados fixo, ou seja, nestas linguagens se você cria um array de tipo int e com tamanho 5, este array será SEMPRE do tipo inteiro e poderá ter SEMPRE no máximo 5 valores.

Já em Python:
 - Dinâmico: Não possuem tamanho fixo, ou seja, podemos criar a lista e simplesmente ir adicionando elementos;
 - Qualquer tipo de dados: Não possuem tipo de dado fixo, ou seja, podemos colocar qualquer tipo de dados;

 As listas em Python são representadas por colchetes: []
"""
type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')

# Podemos facilmente checar se determinado valor está contido na lista
# num = 7
# if num in lista4:
#     print(f'Encontrei o número {num}')
# else:
#     print(f'Não encontrei o número {num}')

# Podemos facilmente ordenar uma lista
# lista1.sort()
# print(lista1)

# Podemos facilmente contar o número de ocorrências de um valor em uma lista
# print(lista1.count(1))
# print(lista5.count('e'))

# Adicionar elementos em listas
"""
Para adicionar elementos em listas, utilizamos a função append

OBS: Com append, nós só conseguimos adicionar um elemento por vez
lista1.append(12, 34, 56) # Erro
"""
# print(lista1)
# lista1.append(42)
# print(lista1)
#
# lista1.append([8, 3, 1]) # Coloca a lista como elemento unico (sublista)
# print(lista1)
#
# if [22, 27, 27] in lista1:
#     print('Encontrei a lista')
# else:
#     print('Não encontrei a lista')
#
# lista1.extend([123, 44, 67]) # Coloca cada elemento da lista como valor adicional à lista
# print(lista1)

# Podemos inserir um novo elemento na lista informando a posição do índice
# OBS: Isso não substitui o valor inicial. O mesmo será deslocado para a direita
# lista1.insert(2, 'Novo Valor')
# print(lista1)

# Podemos facilmente juntar duas listas
# lista1 = lista1 + lista2
# lista1.extend(lista2)
# print(lista1)

# Podemos facilmente reverter uma lista
## Forma 1
# lista1.reverse()
# lista2.reverse()
# print(lista1)
# print(lista2)

## Forma 2
# print(lista1[::-1])
# print(lista2[::-1])

# Copiar uma lista
# lista6 = lista2.copy()
# print(lista6)

# Podemos contar quantos elementos existem dentro da lista
# print(len(lista2))

# Podemos remover facilmente o último elemento de uma lista
# OBS: O pop não somente remove o último elemento, mas também o retorna
# print(lista5)
# lista5.pop()
# print(lista5)

# Podemos remover um elemento pelo índice
# OBS: Os elementos à direita deste índice serão deslocados para a esquerda.
# OBS: Se não houver elemento no índice informado, teremos o erro IndexError.
print(lista5)
lista5.pop(2)
print(lista5)
#1:00:38
