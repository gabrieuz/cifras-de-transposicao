from cifras import encriptar_colunas, desencriptar_colunas, encriptar_rail_fence, desencriptar_rail_fence, encriptar_vigenere, desencriptar_vigenere
import pytest

# Testes unitários para as funções de encriptação e desencriptação das cifras

# Cifra de colunas

# Teste para verificar a encriptação

def test_encriptar_colunas():
    texto = "FUJAM TODOS. Fomos DESCOBERTOS"
    chave = 3
    encriptado = encriptar_colunas(texto, chave, True, True, True)
    assert encriptado == "FATO m SBTUMOSFoDCEOJ D.osEORS"

# Teste para verificar a desencriptação com isSpaceAllowed = True, isSpecialCharAllowed = True e caseSensitive = True
    
def test_desencriptar_colunas():
    texto = "FUJAM TODOS. Fomos DESCOBERTOS"
    chave = 3
    encriptado = encriptar_colunas(texto, chave, True, True, True)
    desencriptado = desencriptar_colunas(encriptado, chave)
    assert desencriptado == texto

# Teste para verificar a desencriptação com isSpaceAllowed = False, isSpecialCharAllowed = False e caseSensitive = False

def test_desencriptar_colunas_restricoes():
    texto = "FUJAM TODOS. Fomos DESCOBERTOS"
    chave = 3
    encriptado = encriptar_colunas(texto, chave, False, False, False)
    desencriptado = desencriptar_colunas(encriptado, chave)
    assert desencriptado == "FUJAMTODOSFOMOSDESCOBERTOS"


# Testes para a cifra de cerca (rail fence)

def test_encriptar_desencriptar_rail_fence():
    texto = "A WIZARD IS NEVER LATE"
    chave = 2
    encriptado = encriptar_rail_fence(texto, chave, True, True, True)
    desencriptado = desencriptar_rail_fence(encriptado, chave)
    assert desencriptado == texto


# Testes para a cifra de Vigenère

def test_encriptar_desencriptar_vigenere():
    texto = "ATACARBASESUL"
    chave = "LIMAO"
    encriptado = encriptar_vigenere(texto, chave)
    desencriptado = desencriptar_vigenere(encriptado, chave)
    assert desencriptado == texto
