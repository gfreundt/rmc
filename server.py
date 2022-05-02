from flask import Flask, render_template
import socket
import os

app = Flask(__name__, static_url_path="", static_folder="static/images")
local_ip = socket.gethostbyname(socket.gethostname())

# Web page endpoints

# HOME
@app.route("/")
def home():
    return render_template("home.html")


# Quienes Somos --> Lucho
@app.route("/lucho")
def lucho():
    return render_template("lucho.html")


# Quienes Somos --> Producción
@app.route("/produccion")
def produccion():
    return render_template("produccion.html")


def main():
    app.run(host=local_ip, debug=True)


if __name__ == "__main__":
    main()
