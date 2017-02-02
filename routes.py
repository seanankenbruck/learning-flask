from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/about")
def about():
  return render_template("about.html")

@app.route("/info")
	def test():
		return test

if __name__ == "__main__":
	app.run(debug=True)