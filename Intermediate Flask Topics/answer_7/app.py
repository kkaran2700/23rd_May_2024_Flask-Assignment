# 7. Integrate a SQLite database with Flask to perform CRUD operations on a list of items.

from flask import Flask, render_template, request, redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///items.db'
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(25), nullable = False)

@app.route('/')
def index():
    items = Item.query.all()
    return render_template('index.html', items=items)

@app.route('/add', methods=['POST'])
def add_item():
    name = request.form["name"]
    new_item = Item(name = name)
    db.session.add(new_item)
    db.session.commit()
    return redirect(url_for("index"))


@app.route('/update/<int:id>', methods=['POST'])
def update_item(id):
    item = Item.query.get_or_404(id)
    item.name = request.form['name']
    db.session.commit()
    return redirect(url_for('index'))




@app.route('/delete/<int:id>')
def delete_item(id):
    item = Item.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('index'))
    



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
