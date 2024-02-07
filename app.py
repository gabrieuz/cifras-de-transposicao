from flask import Flask, render_template, request
from cifras import encriptar_colunas, desencriptar_colunas, encriptar_rail_fence, desencriptar_rail_fence, encriptar_vigenere, desencriptar_vigenere

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cifra-colunas', methods=['POST'])
def cifra_colunas():
    texto = request.form['texto']
    chave = request.form['chave'].strip()  # Remova espaços em branco extras
    if not chave:  # Verifique se a chave está vazia
        return render_template('erro.html', mensagem='A chave não pode estar vazia')

    if not chave.isdigit():  # Verifique se a chave contém apenas dígitos
        return render_template('erro.html', mensagem='A chave deve ser um número inteiro')

    chave = int(chave)  # Converta para um número inteiro

    isSpaceAllowed = 'spaceAllowed' in request.form
    isSpecialCharAllowed = 'specialCharAllowed' in request.form
    caseSensitive = 'caseSensitive' in request.form

    cifrado = encriptar_colunas(
        texto, chave, isSpaceAllowed, isSpecialCharAllowed, caseSensitive)
    return render_template('resultado.html', cifrado=cifrado)

@app.route('/decifra-colunas', methods=['POST'])
def decifra_colunas():
    texto = request.form['texto']
    chave = int(request.form['chave'])

    decifrado = desencriptar_colunas(texto, chave)
    return render_template('resultado.html', decifrado=decifrado)

if __name__ == '__main__':
    app.run(debug=True)
