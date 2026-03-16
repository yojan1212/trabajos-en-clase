from flask import Flask
import random

¿¿
app = Flask(__name__)

@app.route("/")
def inicio ():
    return "<h1> Bienveneido a la pagina web </h1>" \
    "<p> Escribe una pregunta en la barra de direcciones asi: /pregunta/sere_un_hacker </p>"\

if __name__ == "__main__":
    app.run(debug=True)


