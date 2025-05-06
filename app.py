from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    datos = [
        {'id':1,
         'name':'Vrouqen',
         'description':'Me gusta programar'
         },
         {'id':2,
         'name':'Nico',
         'description':'Hola'
         },
         {'id':3,
         'name':'Bryan',
         'description':'Hola como estás'
         },
         {'id':4,
         'name':'Derek',
         'description':'No confíen en mí'
         }
    ]
    return render_template("index.html", datos=datos)

if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0", port = "555")