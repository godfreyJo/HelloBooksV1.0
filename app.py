from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/send', methods=['GET', 'POST'])
def send():
	if request.method == 'POST':
		email = request.form['email']
		password = request.form['password']
		# gridradios = request.form['gridradios']
		# checkbox = request.form['checkbox']
		# button = request.form['button']

		return render_template('signup.html', age = age, email = email,
			password = password, gridradios = gridradios , checkbox = checkbox,
			button = button)

		return render_template('index.html')


if __name__ == "__main__":
	app.run()