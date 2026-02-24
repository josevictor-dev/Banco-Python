def poema(data_dia, *args, **kwargs):
    texto = '\n'.join(args)
    data = data_dia.upper()
    metadados ='\n'.join([f'{chave.title().upper()}: {valor}' for chave, valor in kwargs.items()])
    print(f'{data},\n{texto}, \n{metadados}')


poema(
'Fevereiro de 2025',
'Brasil',
'Acima de tudo',
'Deus a cima de todos',

'autor = Tim Maia',
'sobrenome=pedro',

)
