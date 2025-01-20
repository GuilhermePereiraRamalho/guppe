""""
Recebendo dados do usuario
"""
# Entrada de dados
# print("Qual seu nome? ")
# nome = input()

nome = input("Qual seu nome?")

# Exemplo de print antigo 2.x
# print("Seja bem-vindo(a) %s" % nome)

# Exemplo de print moderno 3.x
# print("Seja bem-vindo(a) {0}".format(nome))

# Exemplo de print 'mais atual
print(f"Seja bem-vindo(a) {nome}")

# print("Qual sua idade? ")
# idade = input()

idade = input('Qual sua idade?')

# Exemplo de print antigo
# print("%s tem %s anos" % (nome, idade))

# Exemplo de print moderno 3.x
# print("{0} tem {1} anos".format(nome, idade))

# Exemplo de print 'mais atual
print(f"{nome} tem {idade} anos")

print(f'{nome} nasceu em {2025 - int(idade)}')
