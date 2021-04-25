from flask import Flask, flash, redirect, render_template, request, session, abort

app = Flask(__name__, template_folder="template")

@app.route("/")
def index():
    return "Flask App!"

@app.route("/profile/<string:name>")
def profile(name):
    return render_template("name.html", name=name)
    # return "<h1> hello {} </h1>".format(name)

if __name__ == "__main__":
    app.run()
    