from flask import Flask, render_template, request


app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app = Flask(__name__)



# ------------------------------------------ Model ------------------------------------------
class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String)
    plate = db.Column(db.String(25))    
    timestamp = db.Column(db.DateTime,  default=db.func.current_timestamp())

    def __repr__(self):
        return f'Car <{self.plate}>'


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