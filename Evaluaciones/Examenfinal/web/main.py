from flask import Flask, request, make_response, redirect, render_template, url_for

app = Flask(__name__)

@app.route("/")
def mainRoute():
    return redirect(url_for("homeRoute"))

@app.route("/home")
def homeRoute():
    return render_template("home.html")

@app.route("/Doctores")
def doctoresRoute():
    return render_template("doctores.html")

@app.route("/Contactanos")
def contactanosRoute():
    return render_template("contactanos.html")

@app.route("/Conocenos")
def conocenosRoute():
    return render_template("conocenos.html")

@app.route("/Pacientes")
def pacientesRoute():
    return render_template("pacientes.html")

@app.route("/Curioso")
def curiosoRoute():
    return render_template("curioso.html")

if (__name__ == "__main__"):
    app.run()