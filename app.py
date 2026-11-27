from flask import Flask, render_template, request, redirect
import mysql.connector
from data import varer,ukensmeny,kontakt


app = Flask(__name__)

def get_conn():
    return mysql.connector.connect(
        host="localhost",
        user="Axel",
        password="Passord123$",
        database="login"
    )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/meny')
def meny():
    return render_template('meny.html', ukensmeny=ukensmeny)

@app.route('/varer')
def vis_varer():
    return render_template('varer.html', varer=varer)

@app.route('/kontakter')
def kontakter():
    return render_template('kontakliste.html', kontakt=kontakt)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        navn = request.form["navn"]
        brukernavn = request.form["brukernavn"]
        passord = request.form["passord"]

        conn = get_conn()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO kunder (navn, brukernavn, passord) VALUES (%s, %s, %s)",
            (navn, brukernavn, passord)
        )
        conn.commit()
        cur.close()
        conn.close()

        return redirect("/login")

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    feil = None
    if request.method == "POST":
        brukernavn = request.form["brukernavn"]
        passord = request.form["passord"]

        conn = get_conn()
        cur = conn.cursor()
        cur.execute(
            "SELECT navn FROM kunder WHERE brukernavn=%s AND passord=%s",
            (brukernavn, passord)
        )
        user = cur.fetchone()
        cur.close()
        conn.close()

        if user:
            return render_template("welcome.html", name=user[0])
        else:
            feil = "Feil brukernavn eller passord"

    return render_template("login.html", feil=feil)


if __name__ == "__main__":
    app.run(debug=True)