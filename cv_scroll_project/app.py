from models import User, db
from werkzeug.security import check_password_hash, generate_password_hash
from flask import Flask, redirect, render_template, request, url_for, flash, session, make_response
import os
from flask_mail import Mail, Message
from os import getenv
from flask_login import LoginManager, login_user, login_required, current_user, logout_user
from flask_login import LoginManager
from datetime import datetime
from flask_admin import Admin
from adminview import MyAdminIndexView, ReservationView, MyModelView, ToursView
from api_bp.api import api_bp
from models import *
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
app.config['FLASK_ADMIN_SWATCH'] = 'simplex'  # устанавливаем тему админки(можно выбрать тут https://bootswatch.com/3/)
db.init_app(app)
mail = Mail(app)
# -----------------------------------------------------------------------------------------
login_manager = LoginManager()
login_manager.init_app(app)

#-Работа с админкой-#
admin = Admin(app, index_view=MyAdminIndexView(), name='ExampleStore',
              template_mode='bootstrap3') 
admin.add_view(MyModelView(User, db.session))
admin.add_view(ToursView(Tours, db.session))
admin.add_view(ReservationView(Reservation, db.session))


app.register_blueprint(api_bp, url_prefix="/api")

#-Работа с юзером-#
#--------------------------------------------------------------------------------------
@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == user_id).first()

#-Основные страницы-#
#--------------------------------------------------------------------------------------
@app.route('/home')
@app.route('/index')
@app.route('/')
def index():
    session.clear()
    session.modified = True
    session["Booking"] = {'items': {}}
    session["Delayed"] = {'items': {}}
    print(session)
    return render_template('index.html')

@app.route('/signin', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        print(f"Received email: {email}")  # Это 
        password = request.form.get('password')
        try:
            user = User.query.filter(User.email == email).one()
        except:
            error_message = f"User not found for email: {email}"
            return make_response(error_message)


        if check_password_hash(user.password,password): 
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

        # Проверяем существует ли уже пользователь с таким email
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return "Пользователь с таким email уже существует"

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
    else:
        return render_template('signup.html')

    
@app.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/profile')
def profile():
    if 'username' in session:
        return render_template('profile.html', username=session['username'], user_email=session['user_email'])
    else:
        return redirect(url_for('login'))


@app.route('/about')
def about():
    return render_template('about.html')


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        email = request.form.get("email")
        phone = request.form.get("phone")
        message = request.form.get("message")
        tours = [tour for tour in tours]
        msg = Message("Актуальные цены на туры", recipients=[email])
        msg.html = render_template('email.html', tours=tours, phone=phone, message=message)
        mail.send(msg)
        return redirect('/index')
    return render_template('contact.html')

@app.route('/test')
def test():
    print(current_user.is_authenticated)
    return current_user.get_id()

#-Работа с турами-#
#--------------------------------------------------------------------------------------

@app.route('/catalog')
def catalog():
    tours = Tours.query.all()
    print(tours)
    return render_template('catalog.html', tours=tours) 

@app.route('/item/<int:tour_id>', methods=['GET', 'POST'])
def show_item(tour_id: int):
    if request.method == 'POST':
        item = Tours.query.filter(Tours.id == tour_id).first()
        return render_template('item.html', item=item)
    return make_response("Данную страницу можно посетить только после посещения каталога", 404) 

@app.route('/add_to_delayed/<int:tour_id>', methods=['GET', 'POST'])
def add_to_delayed(tour_id: int):
    if request.method == 'POST':
        if "Delayed" in session:
            if not str(tour_id) in session["Delayed"]["items"]:
                session["Delayed"]["items"][str(tour_id)] = {"item": tour_id, "qty": 1}
                session.modified = True
            else:
                session["Delayed"]["items"][str(tour_id)]["qty"] += 1
                session.modified = True
        return render_template("delayed.html", delayed_tours=session["Delayed"])
    return redirect("/catalog")

@app.route("/delayed")
def delayed():
    if "Delayed" in session:
        session["Delayed"]["total"] = 0
        for tour_id in session["Delayed"]["items"]:
            tour = Tours.query.filter(Tours.id == tour_id).first()
            session["Delayed"]["items"][tour_id] = {"item": tour.name,
                                                    "qty": session["Delayed"]["items"][tour_id]["qty"],
                                                    "price": tour.price * session["Delayed"]["items"][tour_id]["qty"]}
            session.modified = True
            session["Delayed"]["total"] += session["Delayed"]["items"][tour_id]["price"]
        return render_template("delayed.html", delayed_tours=session["Delayed"])
    return make_response("Delayed session not found", 404)

@app.route("/remove_item/")
def remove_from_delayed():
    tour_id = request.args.get("tour_id")
    item = session["Delayed"]["items"].pop(str(tour_id))
    session.modified = True
    return redirect("/delayed")

@app.route('/article/<name>', methods=["GET", 'POST'])
def article(name):
    if "Booking" in session:
        if not name in session["Booking"]:
            session["Booking"][name] = {"name":name, "qty":1}
            session.modified = True
        else:
            session["Booking"][name]['qty'] += 1
            session.modified = True
    return render_template('article.html', name=name)


@app.route('/add_to_booking/<int:tour_id>', methods=["GET", 'POST'])
def add_to_booking(tour_id: int):
    if request.method == 'POST':
        if "Booking" in session:
            if str(tour_id) not in session["Booking"]:
                session["Booking"][str(tour_id)] = {"tour": tour_id, "qty": 1}
            else:
                session["Booking"][str(tour_id)]['qty'] += 1
        else:
            session["Booking"] = {str(tour_id): {"tour": tour_id, "qty": 1}}
    return session['Booking']

@app.route('/booking')
def booking():
    return render_template("booking.html", booking=session["Booking"])

#-Куки и сессии-#
#--------------------------------------------------------------------------------------

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

if __name__ == '__main__':
    app.run(debug=True)