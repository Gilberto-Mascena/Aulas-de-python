# if / elif / else
# se / se não se / se não

entrada = input('Você quer "entrar" ou "sair"? ')

# The condition in python the indentation is very important
if entrada == 'entrar':
    print('Você entrou no sistema')
elif entrada == 'sair':
    print('Você saiu do sistema')
else:
    print('Você não escolheu uma opção válida')