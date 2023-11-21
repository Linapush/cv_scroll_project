from models import User, db
from werkzeug.security import check_password_hash, generate_password_hash

from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://valun:123@localhost/test_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.route('/home')
@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        pass
    else:
        return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        password = generate_password_hash(password, 'sha256')
        new_user = User(name=name, email=email, password=password)
        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect('/login')
        except:
            return "Добавление не удалось"
    else:
        return render_template('register.html')


@app.route('/catalog')
def catalog():
    return 'catalog'


@app.route('/item')
def item():
    return 'item'


if __name__ == '__main__':
    app.run(debug=True)
