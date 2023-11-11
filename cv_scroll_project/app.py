from models import User, db
from werkzeug.security import check_password_hash, generate_password_hash
from flask import Flask, redirect, render_template, request, url_for, flash, session, make_response
import os
from flask_mail import Mail, Message
from os import getenv
from flask_login import LoginManager, login_user, login_required, current_user, logout_user
from flask_login import LoginManager
from datetime import datetime

# from api_bp.api import api_bp
# psql -h 127.0.0.1 -p 5434 -U lina project_db -f init_db.ddl

# -----------------------------------------------------------------------------------------
app = Flask(__name__)
login_manager = LoginManager()
# -----------------------------------------------------------------------------------------
login_manager.init_app(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://lina:sirius@localhost:5434/project_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.environ.get('SECRET_KEY')
app.config['MAIL_SERVER'] = "smtp.gmail.com"
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('mail')
app.config['MAIL_PASSWORD'] = os.environ.get('password')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('mail')
db.init_app(app)
mail = Mail(app)
# -----------------------------------------------------------------------------------------
login_manager = LoginManager()
login_manager.init_app(app)
# get_id(), is_authenticated(), is_active(), is_anonimus()
# app.register_blueprint(api_bp, url_prefix="api")

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == user_id).first()

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html', username=session['username'], user_email=session['user_email'])

@app.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/home')
@app.route('/index')
@app.route('/')
def index():
    session.clear()
    session.modified = True
    session["Cart"] = {}
    print(session)
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        try:
            user = User.query.filter(User.email == email).one() # делаем запрос к бд, находим по емецлу
        except:
            return 'User not found'
        if check_password_hash(user.password,password): # автоматическое генерировние ключа,
            if user.role == 2:
                login_user(user)
                return render_template('index.html', username=user.name, email=user.email)
            else:
                return "Admin"
        else:
            return redirect('/login')         
    return render_template('sign_in.html')


# добавить проверку на то, что пользователь с таким логином уже существует

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        password = generate_password_hash(password)
        new_user = User(name=name, email=email, password=password, role=2)
        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect("/signin")
        except Exception as e:
            print(e)
            return "Добавление не удалось"
        
    # добавить проверку на то, что пользователь с таким логином уже существует  
    else:
        return render_template('signup.html')

@app.route('/signin', methods=['POST', 'GET'])
def signin():
    """Авторизация"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        try:
            user = User.query.filter(User.email == username).one()
        except Exception as e:
            flash("Пользователь с указанным логином не найден")
            print(e)
            return redirect("/signin")
        if check_password_hash(user.password, password):
            # Добавляем пользователя в сессию
            session['username'] = user.name
            session['user_email'] = user.email
            return render_template('index.html', username=user.name, )
        else:
            flash("Пароль не верен")
            return redirect("/signin")
    return render_template("sign_in.html")


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/articles')
def show_articles():
    return "Demo Articles"


@app.route('/catalog')
def catalog():
    return render_template('catalog.html')


@app.route('/item')
def item():
    return render_template('item.html')

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        email = request.form.get("email")
        phone = request.form.get("phone")
        message = request.form.get("message")

        # Соберем данные об экскурсиях (это должно быть заменено на вашу реальную логику для получения данных об экскурсиях)
        tours = [{"title": "Тур 1", "price": "300$", "link": "/templates/tour1.html"},
                {"title": "Тур 2", "price": "450$", "link": "/templates/tour2.html"}]
        msg = Message("Актуальные цены на туры", recipients=[email])
        msg.html = render_template('email.html', tours=tours, phone=phone, message=message)
        mail.send(msg)
        return redirect('/index')
    return render_template('contact.html')

@app.route('/test')
def test():
    print(current_user.is_authenticated)
    return current_user.get_id()


# @app.route('/make_order')
# def make_order():
#     if 'Cart' in session and session["Cart"]["total"] != 0:
#         if current_user.is_authenticated:
#             new_order  = Order(user_id = current_user.get_id(),
#                                date = datetime.now(),
#                                total = session['Cart']['items'])
#             for product_id in session['Cart']['items']:
#                 for i in range(session['Cart']['items'][product_id]['qty']):
#                     product = Products.query.filter(Products.id == product_id).first()
#                     new.order

@app.route('/cookies')
def cookies():
    res = make_response('Посылки тебе куку, храни ее')
    res.set_cookie("Name", "Oleg", max_age=60*60*24*365)
    return res 

@app.route('/show_cookies')
def show():
    if request.cookies.get('Name'):
        return 'Hello' + request.cookies.get('Name')
    else:
        return "Кук нет"
    
@app.route('/delete_cookies')
def delete_cookies():
    res = make_response('Мы тебя удаляем, куки')
    res.set_cookie('Name', 'asdas', max_age=0)
    return res

@app.route('/counter')
def counter():
    if "visits" in session:
        session["visits"] = session["visits"] + 1
    else:
        session["visits"] = 1
    return "Вы были на этой странице " + str(session.get("visits"))

@app.route('/article/<name>', methods=["GET", 'POST'])
def article(name):
    if "Cart" in session:
        if not name in session["Cart"]:
            session["Cart"][name] = {"name":name, "qty":1}
            session.modified = True
        else:
            session["Cart"][name]['qty'] += 1
            session.modified = True
    return render_template('article.html', name=name)


@app.route('/add_to_cart/<int:product_id>', methods=["GET", 'POST'])
def add_to_cart(product_id:int):
    if request.method == 'POST':
        if "Cart" in session:
            if not str(product_id) in session["Cart"]:
                session["Cart"[str(product_id)]] = {"product": product_id, "qty": 1}
                session.modified = True
            else:
                session["Cart"][str(product_id)]['qty'] += 1
                session.modified = True
        return session['Cart']
    

@app.route('/cart')
def cart():
    return render_template("cart.html", cart=session["Cart"])

if __name__ == '__main__':
    app.run(debug=True)