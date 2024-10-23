from flask import Flask,request,  render_template, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/index.html")
def inicio():
    return render_template("index.html")

@app.route("/quienes.html")
def quienes():
    return render_template("quienes.html")

@app.route("/servicio.html")
def servicio():
    return render_template("servicio.html")

@app.route("/noticias.html")
def noticias():
    return render_template("noticias.html")

@app.route("/contacto.html")
def contactos():
    return render_template("contacto.html")

if __name__ == '__main__':
    app.run(debug=True)

