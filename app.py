from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Ruta principal para mostrar el frontend
@app.route("/")
def index():
    return render_template("index.html")

# Ruta para la API que devuelve los datos
@app.route("/api", methods=['GET'])
def load_user():
    datos = [
        {'id': 1, 'name': 'Vrouqen', 'description': 'Me gusta programar'},
        {'id': 2, 'name': 'David', 'description': 'Hola'},
        {'id': 3, 'name': 'Allan1', 'description': 'Hola como estás'},
        {'id': 4, 'name': 'Kevin', 'description': 'No confíen en mí'}
    ]
    return jsonify({'result': datos})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=999)
