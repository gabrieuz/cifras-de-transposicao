from flask import Flask, render_template, request, jsonify
from cifras import encriptar_colunas, desencriptar_colunas, encriptar_rail_fence, desencriptar_rail_fence, encriptar_vigenere, desencriptar_vigenere

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cifra-colunas', methods=['POST'])
def cifra_colunas():
    texto = request.form['texto']
    chave = request.form['chave'].strip()
    if not chave:
        return jsonify({'error': 'A chave não pode estar vazia'})

    if not chave.isdigit():
        return jsonify({'error': 'A chave deve ser um número inteiro'})

    chave = int(chave)

    isSpaceAllowed = 'spaceAllowed' in request.form
    isSpecialCharAllowed = 'specialCharAllowed' in request.form
    caseSensitive = 'caseSensitive' in request.form

    cifrado = encriptar_colunas(
        texto, chave, isSpaceAllowed, isSpecialCharAllowed, caseSensitive)
    return jsonify({'cifrado': cifrado})


@app.route('/decifra-colunas', methods=['POST'])
def decifra_colunas():
    texto = request.form['texto']
    chave = request.form['chave'].strip()

    if not chave:
        return jsonify({'error': 'A chave não pode estar vazia'})

    if not chave.isdigit():
        return jsonify({'error': 'A chave deve ser um número inteiro'})

    chave = int(chave)

    decifrado = desencriptar_colunas(texto, chave)
    return jsonify({'decifrado': decifrado})


if __name__ == '__main__':
    app.run(debug=True)
