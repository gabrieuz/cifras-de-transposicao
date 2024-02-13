from cifras import encriptar_colunas, desencriptar_colunas, encriptar_rail_fence, desencriptar_rail_fence, encriptar_vigenere, desencriptar_vigenere, print_matriz_colunas, print_matriz_zigue_zague, encriptar_blowfish, desencriptar_blowfish

# Visualização dos resultados das cifras

# Cifra de Colunas

encriptado_colunas = encriptar_colunas("FUJAM TODOS. Fomos DESCOBERTOS", 3)
print(f'\nEncriptado Colunas: {encriptado_colunas}')

desencriptado_colunas = desencriptar_colunas(encriptado_colunas, 3)

print(f'Desencriptado Colunas: {desencriptado_colunas}')

print('\nMatriz Colunas:\n')
print_matriz_colunas(encriptado_colunas, 3)

print('_'*50)

# Cifra de Rail Fence

encriptado_rail_fence = encriptar_rail_fence(
    "A WIZARD IS NEVER LATE", 2, True, True, True)
print(f'\nEncriptado Rail Fence: {encriptado_rail_fence}')

desencriptado_rail_fence = desencriptar_rail_fence(encriptado_rail_fence, 2)
print(f'Desencriptado Rail Fence: {desencriptado_rail_fence}')

print('\nMatriz Rail Fence:\n')
print_matriz_zigue_zague(encriptado_rail_fence, 2)

print('_'*50)

# Cifra de Vigenère

encriptado_vigenere = encriptar_vigenere("ATACARBASESUL", "LIMAO")
print(f'\nEncriptado Vigenere: {encriptado_vigenere}')

desencriptado_vigenere = desencriptar_vigenere(encriptado_vigenere, "LIMAO")
print(f'Desencriptado Vigenere: {desencriptado_vigenere}')

print('_'*50)

# Cifra Blowfish

chave = b'Sixteen byte key'
texto_original = b'Texto original a ser cifrado com Blowfish'

texto_cifrado = encriptar_blowfish(texto_original, chave)
print("\nCifrado Blowfish:", texto_cifrado)

texto_decifrado = desencriptar_blowfish(texto_cifrado, chave)
print("Desencriptado Blowfish:", texto_decifrado)

print('_'*50)
