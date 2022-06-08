import flask

from flask import request, jsonify



app = flask.Flask(__name__)
app.config['DEBUG'] = True

# Sample Books


books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'},
     {'id': 3,
     'title': 'River and the Source',
     'author': 'Ogot',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1985'}
]


@app.route('/', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/<int:id>', methods=['GET'])
def get_book(book_id):
    book = [book for book in books if book['id'] == id]
    if len (book) == 0:
        abort(404)
    return jsonify({'books': book[0]})

@app.route('/add_book', methods=['POST'])
def add_income():
  incomes.append(request.get_json())
  return '', 204

app.run()
