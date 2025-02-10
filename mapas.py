"""
Mapas -> Conhecidos em Python como  Dicionários

# Iterar sobre dicionarios
for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'Em {chave} recebi: {receita[chave]}')

# Acessando as chaves
print(receita.keys())

for chave in receita.keys():
    print(receita[chave])

# Acessando valores
print(receita.values())

for valor in receita.values():
    print(valor)

# Desempacotamento de dicionarios
print(receita.items())

for key, value in receita.items():
    print(f'chave={key} e valor={value}')
"""
receita = {'jan': 100, 'fev': 250, 'mar': 400}
print(receita)

# Soma*, valor maximo*, valor mínimo* e tamanho
# * Se os valores forem todos inteiros ou reais
print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))
