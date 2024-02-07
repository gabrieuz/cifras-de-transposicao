# Cifra de Colunas

def encriptar_colunas(texto, chave, isSpaceAllowed=False, isSpecialCharAllowed=False, caseSensitive=False):
    texto = texto.replace(' ', '') if not isSpaceAllowed else texto
    texto = ''.join([i for i in texto if i.isalnum() or isSpecialCharAllowed])
    texto = texto.upper() if not caseSensitive else texto
    texto_cifrado = ''
    for i in range(chave):
        texto_cifrado += texto[i::chave]
    return texto_cifrado

encriptado_colunas = encriptar_colunas("FUJAM TODOS. Fomos DESCOBERTOS", 3, True, True, True)
print(f'Encriptado Colunas: {encriptado_colunas}')

def print_matriz(texto_cifrado, chave):
    num_linhas = len(texto_cifrado) // chave
    if len(texto_cifrado) % chave != 0:
        num_linhas += 1

    for i in range(0, len(texto_cifrado), num_linhas):
        print(' '.join(texto_cifrado[i:i+num_linhas]))

print_matriz(encriptado_colunas, 3)

def desencriptar_colunas(texto_cifrado, chave):
    num_linhas = len(texto_cifrado) // chave
    if len(texto_cifrado) % chave != 0:
        num_linhas += 1

    texto = ''
    for i in range(num_linhas):
        texto += texto_cifrado[i::num_linhas]
    return texto

desencriptado_colunas = desencriptar_colunas(encriptado_colunas, 3)
print(f'Desencriptado Colunas: {desencriptado_colunas}')

# Cifra de Cerca (Rail Fence)

def encriptar_rail_fence(texto, chave, isSpaceAllowed=False, isSpecialCharAllowed=False, caseSensitive=False):
    texto = texto.replace(' ', '') if not isSpaceAllowed else texto
    texto = ''.join([i for i in texto if i.isalnum() or isSpecialCharAllowed])
    texto = texto.upper() if not caseSensitive else texto
    texto_cifrado = ''
    for i in range(chave):
        texto_cifrado += texto[i::chave]
    return texto_cifrado

encriptado_rail_fence = encriptar_rail_fence("A WIZARD IS NEVER LATE", 2, True, True, True)
print(f'Encriptado Rail Fence: {encriptado_rail_fence}')

def print_matriz_zigue_zague(texto_cifrado, chave):
    num_colunas = len(texto_cifrado) // chave
    if len(texto_cifrado) % chave != 0:
        num_colunas += 1

    idx = 0
    for i in range(chave):
        linha = ''
        for j in range(num_colunas):
            if idx < len(texto_cifrado):
                if i != 0 and j == 0:
                    linha += '- '
                linha += texto_cifrado[idx] + ' - '
                idx += 1
        if i != 0:
            linha += '-'
        print(linha.rstrip(' - '))

print_matriz_zigue_zague(encriptado_rail_fence, 2)

def desencriptar_rail_fence(texto_cifrado, chave):
    num_colunas = len(texto_cifrado) // chave
    if len(texto_cifrado) % chave != 0:
        num_colunas += 1

    texto = ''
    for i in range(num_colunas):
        texto += texto_cifrado[i::num_colunas]
    return texto

desencriptado_rail_fence = desencriptar_rail_fence(encriptado_rail_fence, 2)
print(f'Desencriptado Rail Fence: {desencriptado_rail_fence}')

# Cifra de Vigenère

def encriptar_vigenere(texto, chave):
    texto_cifrado = ''
    for i in range(len(texto)):
        texto_cifrado += chr((ord(texto[i]) + ord(chave[i % len(chave)]) - 2 * 65) % 26 + 65)
    return texto_cifrado

encriptado_vigenere = encriptar_vigenere("ATACARBASESUL", "LIMAO")
print(f'Encriptado Vigenere: {encriptado_vigenere}')

def desencriptar_vigenere(texto_cifrado, chave):
    texto = ''
    for i in range(len(texto_cifrado)):
        texto += chr((ord(texto_cifrado[i]) - ord(chave[i % len(chave)]) + 26) % 26 + 65)
    return texto

desencriptado_vigenere = desencriptar_vigenere(encriptado_vigenere, "LIMAO")
print(f'Desencriptado Vigenere: {desencriptado_vigenere}')
