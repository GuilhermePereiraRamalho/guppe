"""
PEP8 - Python Enhancement Proposal

São propostas de melhorias para a linguagem Python

The Zen of Python

import this

A ideia da PEP8 é que possamos escrever codigos Python de forma  Pythônica.

[1] - Utilize Camel Case para nomes de classes -
class MinhaClasse:
    pass

[2] - Utilize nomes em minusculo, separados por underline para funcoes ou variaveis -
def minha_funcao():
    pass

minha_variavel = x

[3] - Utilize 4 espacos para identação!
if 'a' in 'banana':
    print('tem')

[4] - Linhas em branco:
- Separar funções e definicoes de classe com duas linhas em branco;
- Metodos dentro de uma classe devem ser separados com uma unica linha em branco;

[5] - Imports devem sempre ser feitos em linhas separadas(para pacotes diferentes):
# import errado
import sys, os

#import certo
import sys
import os

# nao há problemas em utilizar:
from types import StringType, ListType

# Caso tenha muitos imports de um mesmo pacoete, recomenda-se fazer:
from types import (
    StringType,
    ListType,
    SetType,
    OutroType
)

# importes devem ser colocados no topo do arquivo, logo depois de quaisquer comentarios ou docstrings e antes de constantes ou variaveis globais.

[6] - Espacoes em expressoes e instrucoes:
# nao faca
funcao( algo [ 1 ], { outro: 2 } )
algo (1)
dict ['chave'] = lista [indice]
x              = 1
y              = 3
variavel_longa = 5

# faca:
funcao(algo[1], {outro: 2}
algo(1)
dict['chave'] = lista[indice]
x = 1
y = 3
variavel_longa = 5

[7] - Termine sempre uma instrucao com uma nova linha
"""
import this
