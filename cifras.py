from Crypto.Cipher import DES
from Crypto.Cipher import AES
from Crypto.Cipher import Blowfish
import base64
from Crypto import Random

# Cifra de Colunas

def encriptar_colunas(texto, chave, isSpaceAllowed=False, isSpecialCharAllowed=False, caseSensitive=False):
    texto = texto.replace(' ', '') if not isSpaceAllowed else texto
    texto = ''.join([i for i in texto if i.isalnum() or isSpecialCharAllowed])
    texto = texto.upper() if not caseSensitive else texto
    texto_cifrado = ''
    for i in range(chave):
        texto_cifrado += texto[i::chave]
    return texto_cifrado

def print_matriz_colunas(texto_cifrado, chave):
    num_linhas = len(texto_cifrado) // chave
    if len(texto_cifrado) % chave != 0:
        num_linhas += 1

    for i in range(0, len(texto_cifrado), num_linhas):
        print(' '.join(texto_cifrado[i:i+num_linhas]))

def desencriptar_colunas(texto_cifrado, chave):
    num_linhas = len(texto_cifrado) // chave
    if len(texto_cifrado) % chave != 0:
        num_linhas += 1

    texto = ''
    for i in range(num_linhas):
        texto += texto_cifrado[i::num_linhas]
    return texto


# Cifra de Cerca (Rail Fence)

def encriptar_rail_fence(texto, chave, isSpaceAllowed=False, isSpecialCharAllowed=False, caseSensitive=False):
    texto = texto.replace(' ', '') if not isSpaceAllowed else texto
    texto = ''.join([i for i in texto if i.isalnum() or isSpecialCharAllowed])
    texto = texto.upper() if not caseSensitive else texto
    texto_cifrado = ''
    for i in range(chave):
        texto_cifrado += texto[i::chave]
    return texto_cifrado

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


def desencriptar_rail_fence(texto_cifrado, chave):
    num_colunas = len(texto_cifrado) // chave
    if len(texto_cifrado) % chave != 0:
        num_colunas += 1

    texto = ''
    for i in range(num_colunas):
        texto += texto_cifrado[i::num_colunas]
    return texto

# Cifra de Vigenère

def encriptar_vigenere(texto, chave):
    texto_cifrado = ''
    for i in range(len(texto)):
        texto_cifrado += chr((ord(texto[i]) + ord(chave[i % len(chave)]) - 2 * 65) % 26 + 65)
    return texto_cifrado

def desencriptar_vigenere(texto_cifrado, chave):
    texto = ''
    for i in range(len(texto_cifrado)):
        texto += chr((ord(texto_cifrado[i]) - ord(chave[i % len(chave)]) + 26) % 26 + 65)
    return texto

# Cifra Blowfish

def encriptar_blowfish(texto, chave):

    chave = chave.ljust(16, b'\0')

    iv = Random.new().read(Blowfish.block_size)

    cipher = Blowfish.new(chave, Blowfish.MODE_CBC, iv)

    length = Blowfish.block_size - (len(texto) % Blowfish.block_size)
    texto += bytes([length]) * length

    texto_cifrado = iv + cipher.encrypt(texto)

    return base64.b64encode(texto_cifrado)


def desencriptar_blowfish(texto_cifrado, chave):
    chave = chave.ljust(16, b'\0')

    texto_cifrado = base64.b64decode(texto_cifrado)

    iv = texto_cifrado[:Blowfish.block_size]

    cipher = Blowfish.new(chave, Blowfish.MODE_CBC, iv)

    plain_text = cipher.decrypt(texto_cifrado[Blowfish.block_size:])

    return plain_text[:-plain_text[-1]]

# Cifra AES

def encriptar_aes(texto, chave):    
    chave = chave.ljust(16, b'\0')

    iv = Random.new().read(AES.block_size)

    cipher = AES.new(chave, AES.MODE_CBC, iv)

    length = AES.block_size - (len(texto) % AES.block_size)
    texto += bytes([length]) * length

    texto_cifrado = iv + cipher.encrypt(texto)

    return base64.b64encode(texto_cifrado)


def desencriptar_aes(texto_cifrado, chave):
    chave = chave.ljust(16, b'\0')

    texto_cifrado = base64.b64decode(texto_cifrado)

    iv = texto_cifrado[:AES.block_size]

    cipher = AES.new(chave, AES.MODE_CBC, iv)

    plain_text = cipher.decrypt(texto_cifrado[AES.block_size:])

    return plain_text[:-plain_text[-1]]

# Cifra DES

def encriptar_des(texto, chave):
    chave = chave.ljust(8, b'\0')

    iv = Random.new().read(DES.block_size)

    cipher = DES.new(chave, DES.MODE_CBC, iv)

    length = DES.block_size - (len(texto) % DES.block_size)
    texto += bytes([length]) * length

    texto_cifrado = iv + cipher.encrypt(texto)

    return base64.b64encode(texto_cifrado)


def desencriptar_des(texto_cifrado, chave):
    chave = chave.ljust(8, b'\0')

    texto_cifrado = base64.b64decode(texto_cifrado)

    iv = texto_cifrado[:DES.block_size]

    cipher = DES.new(chave, DES.MODE_CBC, iv)

    plain_text = cipher.decrypt(texto_cifrado[DES.block_size:])

    return plain_text[:-plain_text[-1]]


