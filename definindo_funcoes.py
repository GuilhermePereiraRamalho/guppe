"""
Definindo Funções

- Funções são pequenas partes de código que realizam tarefas especificas;
- Pode ou não receber entradas de dados e retornar uma saida de dados;
- São muito uteis para executar procedimentos similares por repetidas vezes;

OBS: Se você escrever uma função que realiza várias tarefas dentro dela é bom fazer uma verificação para que a função seja simplificada

Já utilizamos várias funções:
- print()
- len()
- min()
- max()
- count()
- e muitas outras

# Exemplo de utilização de funções
cores = ['verde', 'amarelo', 'azul', 'branco']

# Utilizando a função integrada (Build-in) do Python print()
# print(cores)

curso = 'Programação em Python: Essencial'

# print(curso)

cores.append('roxo')

# print(cores)

cores.clear()
# print(cores)


# print(help(print))
# DRY - Don`t Repeat Yourself
"""

# Mas então, como definir funções?
"""
Em Python, a forma geral de definir uma função é:

def nome_da_funcao(parametros_de_entrada):
    bloco_da_funcao
    
Onde:
nome_da_funcao -> SEMPRE, com letras minúsculas, e se for nome composto, separado por underline(Snake case)
parametros_de_entrada -> Opcionais, onde tendo mais de um, cada um separado por virgula, podendo ser opcionais ou não;
bloco_da_funcao -> Também chamado de corpo da função ou implementação, é onde o processamento da função acontece. Neste bloco, pode ter u não retorno da função.

OBS: Veja que para definir uma função, utilizamos a palavra reservada 'def' informando ao Python que estamos definindo uma função. Também abirmos o bloco de código com o já conhecido dois pontos : que é utilizado em Python para definir blocos
"""

# Definindo a primeira função

def diz_oi():
    print('oi!')

"""
OBS: 
1- Veja que dentro das nossa funções podemos utilizar outras funções;
2- Veja que nossa função só executa 1 tarefa, ou seja, a única coisa que ela faz é dizer oi;
3- Veja que esta função não recebe nenhum parâmetro de entrada;
4- Veja que esta função não retorna nada;
"""

# Chamada de execução
diz_oi()

"""
ATENÇÃO:

Nunca esqu3ça de utilizar o parênteses ao executar uma função.

Exemplo:

# Errado!
diz_oi

# Certo
diz_oi()

# Errado
diz_oi ()
"""

# Exemplo 2
def cantar_parabens():
    print('Parabéns pra você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print('Viva o aniversariante!')

# for n in range(5):
#     cantar_parabens()

# Em Python podemos inclusive criar variáveis do tipo de uma função e executar essa função através da variável
canta = cantar_parabens

canta()
