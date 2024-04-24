from flask import Flask,  redirect, url_for, render_template

app = Flask(__name__)


@app.route("/")
def display():
  return render_template("index.html")


@app.route("/next")
def next():
  return redirect(url_for('display'))


@app.route("/test")
def test():
  return "This is the kachi function"


@app.route("/second")
def second():
  return redirect(url_for('test'))


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True, port=8080)
