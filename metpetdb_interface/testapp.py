from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
@app.route('/test')
def test():
	return render_template("exercise.html")

app.run(debug=True)
