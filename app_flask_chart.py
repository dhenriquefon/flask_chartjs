import flask
from flask import render_template, redirect, url_for

app = flask.Flask(__name__, static_url_path='',
            static_folder='static',
            template_folder='template')
app.config["DEBUG"] = True

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/admin")
def admin():
    return redirect(url_for("home"))

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)