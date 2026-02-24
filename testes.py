texto = 'A mamae mandou'
novo_texto = ''

for letras in texto:
    if 'a' in letras:
       novo_texto += 'z'
    else:    
        novo_texto += letras



    print(novo_texto)