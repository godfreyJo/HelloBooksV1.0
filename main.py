from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/index')
def index():
	return render_template('index.html')


@app.route('/signup')
def login():
	return render_template('signup.html')


@app.route('/AdminLogin')
def AdminLogin():
	return render_template('AdminLogin.html')


if __name__ == "__main__":
	app.run(debug=True)