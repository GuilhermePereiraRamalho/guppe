"""
Estruturas lógicas: and, or, not, is

Operadores unários:
    - not
operadores binários:
    - and, or, is
"""
ativo = False
logado = True

# if ativo and logado:
#     print('Bem-vindo usuário!')
# else:
#     print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')

# if ativo or logado:
#     print('Bem-vindo usuário!')
# else:
#     print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')

if not ativo:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')
else:
    print('Bem-vindo usuário!')
