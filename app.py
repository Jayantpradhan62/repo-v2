from flask import Flask,render_template,jsonify

from data import load_from_database

app = Flask(__name__)


PLANS = [{"id":"1",
         "course":"Data Science",
         "duration":"4 months",
         "Price":"$99 USD"},
        {"id":"2",
           "course":"Full Stack Web Devlopment",
           "duration":"5 months",
           "Price":"$249 USD"},
        {"id":"3",
           "course":"Data Structures and Algorithms",
           "duration":"3 months",
           "Price":"$129 USD"},
        {"id":"4",
           "course":"Game Devlopment",
           "duration":"6 months",
           "Price":"$299 USD"}]


X  = ["hello","hii"]


@app.route('/')
def build():
  PLANES = load_from_database()
  return render_template("we2.html",plans = PLANES)

@app.route('/api/plans')
def plan():
  return jsonify(PLANS)

@app.route('/Data-Science')
def DataScience():
  return render_template("DS.html")

@app.route('/Demo')
def Demo():
  return render_template("Demo.html")


if __name__ == "__main__":
  app.run(host="0.0.0.0",debug=True)