from flask import Flask,  redirect, url_for, render_template,jsonify

app = Flask(__name__)


JOBS = [
  {
    'id': 1,
    'title': 'Data Scientist',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 10,00,000'
  },
  {
    'id': 2,
    'title': 'Data Analyst',
    'location': 'Delhi, India',
    'salary': 'Rs. 15,00,000'
  },
  {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Lagos, Nigeria',
    'salary': 'Ngn. 200,000,00'
  },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'Remote',
    'salary': 'Usd$. 200,000'
  }
]

@app.route("/")
def display():
  return render_template("index.html", jobs=JOBS)

@app.route("/redirect")
def next():
  return redirect(url_for('display'))

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True, port=8080)
