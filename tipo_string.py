"""
Tipo String

Em Python, um dado é considerado do tipo string sempre que:

- Estiver entre àspas simples: 'uma string', '234', 'a', 'True', '42.3'
- Estiver entre àspas duplas: "uma string", "234", "a", "True", "42.3"
- Estiver entre àspas simples triplas: '''uma string''', '''234''', '''a''', '''True''', '''42.3'''
- Estiver entre àspas duplas triplas: igual a esse comentário
"""
# nome = 'Geek University' # mais comum
# nome = "Geek University"
# nome = '''Geek University'''
# nome = """Geek University"""
# print(nome)
# print(type(nome))

# nome = "Gina's bar"
# print(nome)
# print(type(nome))

# nome = 'Angelina \nJolie'
# print(nome)
# print(type(nome))

# nome = """Angelina
# Jolie"""
# print(nome)
# print(type(nome))

# nome = "Angelina \" Jolie"
# print(nome)
# print(type(nome))

nome = 'Geek University'
# print(nome.upper())
# print(nome.lower())
# print(nome.split()) # transforma em uma lista de strings
# print(nome[0:4])
# print(nome[5:15])
# print(nome.split()[0])
# print(nome.split()[1])
print(nome[::-1])
print(nome.replace('G', 'P'))
