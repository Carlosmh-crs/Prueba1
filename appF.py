from flask import Flask, render_template, request

app = Flask(__name__)

# Vista principal / Inicio
@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    if request.method == 'POST':
        numero = request.form.get('numero')
        if numero:
            resultado = int(numero) ** 2
    return render_template('index.html', resultado=resultado)

# Vista "Cargar Datos"
@app.route('/cargar', methods=['GET', 'POST'])
def cargar():
    mensaje = None
    if request.method == 'POST':
        archivo = request.files.get('csvFile')
        if archivo:
            mensaje = f"Archivo '{archivo.filename}' subido correctamente."
            # Aquí podrías procesar el CSV
    return render_template('DataIn.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)