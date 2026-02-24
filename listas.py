def identificar_categoria_gadget(codigo):

    if codigo.startswith('T'):
        return 'Tablet'
    elif codigo.startswith('P'):
        return 'Phone'
    elif codigo.startswith('N'):
        return 'Notebook'
    else:
        return 'unknow'

  
# Leitura da entrada (espera-se uma string representando o código do gadget)
codigo_gadget = input('Codigo').strip().upper()

# Chamada da função e saída do resultado
categoria = identificar_categoria_gadget(codigo_gadget)

print(categoria)  # Deve imprimir uma das categorias ou 'unknown'