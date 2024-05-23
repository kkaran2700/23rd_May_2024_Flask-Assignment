# 9. Create a RESTful API using Flask to perform CRUD operations on resources like books or movies.

from flask import Flask, request, jsonify, abort, render_template

app = Flask(__name__)

# In-memory database to store books
books = []

# Helper function to find a book by ID
def find_book(book_id):
    return next((book for book in books if book['id'] == book_id), None)

# Route to render the main page
@app.route('/')
def index():
    return render_template('index.html')

# Route to render the create book page
@app.route('/create')
def create_book_page():
    return render_template('create_book.html')

# Route to render the update book page
@app.route('/update/<int:book_id>')
def update_book_page(book_id):
    book = find_book(book_id)
    if book is None:
        abort(404)
    return render_template('update_book.html', book=book)

# Route to render the view books page
@app.route('/view')
def view_books_page():
    return render_template('view_books.html')

# Route to get all books
@app.route('/api/books', methods=['GET'])
def get_books():
    return jsonify(books)

# Route to get a specific book by ID
@app.route('/api/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = find_book(book_id)
    if book is None:
        abort(404)
    return jsonify(book)

# Route to create a new book
@app.route('/api/books', methods=['POST'])
def create_book():
    if not request.json or not 'title' in request.json:
        abort(400)
    new_book = {
        'id': len(books) + 1,
        'title': request.json['title'],
        'author': request.json.get('author', ""),
        'published_date': request.json.get('published_date', ""),
        'isbn': request.json.get('isbn', "")
    }
    books.append(new_book)
    return jsonify(new_book), 201

# Route to update an existing book by ID
@app.route('/api/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = find_book(book_id)
    if book is None:
        abort(404)
    if not request.json:
        abort(400)
    book['title'] = request.json.get('title', book['title'])
    book['author'] = request.json.get('author', book['author'])
    book['published_date'] = request.json.get('published_date', book['published_date'])
    book['isbn'] = request.json.get('isbn', book['isbn'])
    return jsonify(book)

# Route to delete a book by ID
@app.route('/api/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = find_book(book_id)
    if book is None:
        abort(404)
    books.remove(book)
    return jsonify({'result': True})

# Error handler for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

# Error handler for 400
@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad request'}), 400

if __name__ == '__main__':
    app.run(debug=True)
