from flask import Flask, render_template

app = Flask(__name__)
JOBS=[
  {
    'id': 1,
    'title': 'xyz',
    'location': 'klli',
    'salary': '111223'
  },
  {
    'id': 2,
    'title': 'abc',
    'location': 'klli',
    'salary': '111223'
  },
  {
    'id': 3,
    'title': 'def',
    'location': 'klli',
    'salary': '111223'
  },
  {
    'id': 4,
    'title': 'klm',
    'location': 'klli',
    'salary': '111223'
  }
]
@app.route("/")
def hello_world():
    return render_template("home.html", jobs=JOBS)


if __name__=='__main__':
  app.run(host='0.0.0.0',debug=True)