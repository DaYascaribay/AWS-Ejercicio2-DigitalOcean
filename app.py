from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Ruta principal para mostrar el frontend
@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=999)
