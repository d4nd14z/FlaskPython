import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route("/")
def main():
    data = {
        "app": os.getenv("APP_NAME"),
        "title": " Home .::. {app} ".format(app=os.getenv("APP_NAME")),
        "texto": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
    }
    return render_template("medtransfer.html", data=data)


@app.route("/upload", methods=["POST"])
def upload():
    mimes = [
        "text/csv",
        "application/vnd.ms-excel",
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    ]
    if request.method == "POST":
        periodo = request.form["periodo"]
        cuenta = request.form["cuenta"]
        f = request.files["formFile"]
        # Validar que el Mime-Type sea un tipo válido
        if f.content_type in mimes:
            filename = secure_filename(f.filename)
            # Validar que exista la ruta UPLOAD_PATH
            if os.path.exists(os.path.join(os.getenv("UPLOAD_PATH"))):
                f.save(os.path.join(os.getenv("UPLOAD_PATH"), filename))
                # Redireccionar a otro metodo (Redireccionar al metodo "procesar")
                return redirect(url_for("procesar"))
            else:
                return "<h1>UPLOAD PATH Error</h1>"
        else:
            return "<h1>Not valid MimeType</h1>"


@app.route("/procesar", methods=["GET"])
def procesar():
    data = {
        "app": os.getenv("APP_NAME"),
        "title": " Home .::. {app} ".format(app=os.getenv("APP_NAME")),
        "texto": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
    }
    return render_template("procesar.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)
