from models import User, db
from werkzeug.security import check_password_hash, generate_password_hash
from flask import Flask, redirect, render_template, request, url_for, flash, session, make_response
import os
from flask_mail import Mail, Message
from os import getenv
from flask_login import LoginManager, login_user, login_required, current_user, logout_user, user_logged_in
from flask_login import LoginManager
from datetime import datetime
from flask_admin import Admin
from adminview import *
from api_bp.api import api_bp
from models import *

# import secrets

# secret_key = secrets.token_urlsafe(16)
# print(secret_key)

# psql -h 127.0.0.1 -p 5434 -U lina project_db -f init_db.ddl

# -----------------------------------------------------------------------------------------
app = Flask(__name__)
app.secret_key = 'q942obV58YWNANSQAa3DvA'
# -----------------------------------------------------------------------------------------
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
# -----------------------------------------------------------------------------------------

admin = Admin(app, index_view=MyAdminIndexView(), name='ExampleStore', template_mode='bootstrap3')
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
@app.route('/admin/tours')
def admin_tours():
    pass

@app.route('/admin/reservation')
def admin_reservation():
    pass

@app.route('/home')
@app.route('/index')
@app.route('/')
def index():
    # session.clear()
    session.modified = True
    session["Delayed"] = {'items': {}}
    session["Booking"] = {'items': {}}
    print(session)
    if current_user.is_authenticated:
        return render_template('index.html', username=current_user.name, email=current_user.email)
    else:
        return render_template('index.html', user_logged_in=user_logged_in)

@app.route('/to_signin', methods=['GET', 'POST'])
def to_signin():
    return redirect('signin')

@app.route('/signin', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        print(f"Received email: {email}")
        password = request.form.get('password')
        try:
            user = User.query.filter(User.email == email).one()
        except:
            error_message = f"User not found for email: {email}"
            return make_response(error_message)

        if check_password_hash(user.password, password):
            if user.role == 2:
                login_user(user)
                return render_template('index.html', username=user.name, email=user.email)
            else:
                login_user(user)
                next_url = request.form.get('next') or url_for('admin')
                return redirect('/admin')
        else:
            flash("Пользователь с указанным логин/паролем не найден")
            return redirect('/login?next=' + request.url)
    return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        existing_user = User.query.filter_by(email=email).first()
        
        if not name or not email or not password:
            flash('Please fill in all the required fields', 'error')
            return redirect(request.url)
            
        if existing_user:
            return "Пользователь с таким email уже существует"

        password = request.form.get("password")
        password = generate_password_hash(password)

        if name == "Admin":
            new_user = User(name=name, email=email, password=password, role=1)
        else:
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
@login_required
def profile():
    if current_user.is_authenticated:
        return render_template('profile.html', username=current_user.name, email=current_user.email)
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
@login_required
def add_to_delayed(tour_id: int):
    print(session)
    if request.method == 'POST':
        if "Delayed" in session:
            tour = Tours.query.filter(Tours.id == tour_id).first()
            if not str(tour_id) in session["Delayed"]["items"]:
                session["Delayed"]["items"][str(tour_id)] = {
                    "item": tour.name,
                    "qty": 1,  # начальное количество
                    "price": tour.price  # начальная цена за один тур
                }
                session.modified = True
            else:
                session["Delayed"]["items"][str(tour_id)]["qty"] += 1
                session["Delayed"]["items"][str(tour_id)]["price"] = tour.price * session["Delayed"]["items"][str(tour_id)]["qty"]
                session.modified = True

        print(session['Delayed'])
        return render_template("delayed.html", delayed_tours=session["Delayed"])
    return redirect("/catalog")

@app.route("/delayed")
def delayed():
    print(session)
    if "Delayed" in session:
        session["Delayed"]["total"] = 0
        for tour_id in session["Delayed"]["items"]:
            tour = Tours.query.filter(Tours.id == tour_id).first()
            session["Delayed"]["items"][tour_id] = {"item": tour.name,
                                                    "qty": session["Delayed"]["items"][tour_id]["qty"],
                                                    "price": tour.price * session["Delayed"]["items"][tour_id]["qty"]}
            session.modified = True
            session["Delayed"]["total"] += session["Delayed"]["items"][tour_id]["price"]
            session.modified = True
        return render_template("delayed.html", delayed_tours=session["Delayed"])
    print("Delayed not found in session")
    return make_response("Delayed session not found", 404)


@app.route('/remove_from_delayed/<int:tour_id>', methods=['POST'])
def remove_from_delayed(tour_id: int):
    if "Delayed" in session and str(tour_id) in session["Delayed"]["items"]:
        del session["Delayed"]["items"][str(tour_id)]
        session.modified = True
    return redirect("/delayed")

##################################################################################


@app.route('/add_to_booking/<int:tour_id>', methods=["GET", 'POST'])
@login_required
def add_to_booking(tour_id: int):
    print(session)
    if request.method == 'POST':
        if current_user.is_authenticated:
            if "Delayed" in session and "Booking" in session:
                    tour = Tours.query.filter(Tours.id == tour_id).first()
                    reservation = Reservation(date=datetime.now(), status="Booked", payment_status="Pending", tour=tour, user_id=current_user.id)
                    db.session.add(reservation)
                    db.session.commit()
                    session['Booking'] = {tour.id:{'reservation_id':reservation.id}}
                    session.modified = True
        else:
                flash('You should be an authorized user!')
                return redirect(url_for('login', next=request.url))
    return redirect("/booking")

# @app.route('/booking')
# def booking():
#     if "Booking" in session:
#         session["Booking"]["total"] = 0
#         for rv_id in session["Booking"]["items"]:
#             reservation = Reservation.query.filter(Reservation.id == rv_id).first()

#             session["Booking"]["items"][rv_id] = {"item": reservation.id,
#                                                     "qty": session["Delayed"]["items"][rv_id]["qty"],


#             }
#             session.modified = True
#         return render_template("booking.html", booking=session["Booking"])
#     return make_response("Delayed session not found", 404)

@app.route('/booking')
def booking():
    print(session)
    if "Booking" in session and "Delayed" in session:
        for tour_id in session["Booking"]:
            tour = Tours.query.filter(Tours.id == tour_id).first()
            try:
                reservation = Reservation.query.filter(Reservation.id == session["Booking"][tour_id]["reservation_id"]).first()
            except:
                return redirect('/catalog', flash('Сначала посетите каталог!'))
            date_only = reservation.date.date()
            session["Booking"][tour_id] = {"date": date_only,
                                                    "item": tour.name,
                                                    "status": reservation.status,
                                                    "payment_status": reservation.payment_status,
                                                    "price": tour.price,
                                                    "reservation_id": reservation.id
                                                    }
            session.modified = True
            print(session["Booking"])
        return render_template("booking.html", booking=session["Booking"])
    return make_response("Booking session not found", 404)


@app.route('/remove_from_booking/<tour_id>', methods=['POST'])
def remove_from_booking(tour_id):
    print(session)
    if tour_id in session["Booking"]:
        if session["Booking"][tour_id] == 1:
            reservation_id = session["Booking"][tour_id]["reservation_id"]
            reservation = Reservation.query.filter_by(id=reservation_id).first()
            db.session.delete(reservation)
            db.session.commit()
            del session["Booking"][tour_id]
        else:
            session["Booking"][tour_id] = 1
        flash("Тур был удален из Вашей брони!")
    return redirect("/booking")

# Paid #

# @app.route('/payment/<tour_id>', methods = ['GET', 'POST'])
# def payment(tour_id):
#     if "Booking" in session and tour_id in session["Booking"]:
#         tour = Tours.query.filter(Tours.id == tour_id).first()
#         reservation_id = int(session["Booking"][tour_id]["reservation_id"])
#         reservation = Reservation(date=datetime.now(), status="Completed", payment_status="Paid", tour=tour, user_id=current_user.id, reservation_id = reservation_id)
#         db.session.add(reservation)
#         db.session.commit()
#         session['Booking'] = {tour.id:{'reservation_id':reservation.id}}
#         session.modified = True
#         # reservation = Reservation.query.filter(Reservation.id == reservation_id).first()
#         return render_template("catalog.html", tour=tour, reservation=reservation, payment_form=PaymentForm())
#     else:
#         flash("У Вас еше нет забронированных туров!")
#         return redirect(url_for("catalog"))

from forms import PaymentForm

# import logging
# logging.basicConfig()
# logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)



@app.route('/payment/<tour_id>', methods=['GET', 'POST'])
def process_payment(tour_id):
    print('что-то')
    form = PaymentForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        print('Валидация формы')
        try:
            tour = Tours.query.get(tour_id)
            if tour is None:
                flash("Ошибка: Тур не найден")
                return redirect(url_for('catalog'))
            amount = form.amount.data
            user = User.query.filter(User.id == current_user.get_id()).first()
            print(user)
            if user:
                if user.amount >= amount:
                    reservation_id = session["Booking"][tour_id]["reservation_id"]
                    reservation = Reservation.query.filter_by(id=reservation_id).first()
                    if reservation:
                        reservation.payment_status = "Paid"
                        user.amount -= amount
                        reservation.verified = True
                        user.verified = True
                        db.session.commit()
                        msg = Message('Бронирование и оплата тура', recipients=[user.email])
                        msg.body = f"Вы успешно забронировали и оплатили тур tour.title на сумму form.amount.data."
                        mail.send(msg)
                        flash("Оплата прошла успешно! Письмо с информацией о бронировании и оплате отправлено на вашу почту.")
                        return redirect(url_for('catalog'))
                    else:
                        flash("Ошибка: Невозможно найти бронирование")
                else:
                    flash("Ошибка: Недостаточно средств на балансе")
        except Exception as e:
                print(e)
                flash(f"Не удалось выполнить оплату. Пожалуйста, попробуйте еще раз или обратитесь в службу поддержки.")
                app.logger.error("Failed to process payment", exc_info=True)
    return render_template('payment.html', form=form, tour_id=tour_id)

@app.route('/account/recharge', methods=['POST'])
@login_required
def recharge():
    print(session)
    amount = float(request.form.get('amount'))
    current_user.amount += amount
    db.session.commit()
    flash('Баланс успешно пополнен')
    return redirect(url_for('profile'))

# @app.route('/confirm_payment/<reservation_id>')
# def confirm_payment(reservation_id):
#     reservation = Reservation.query.filter(Reservation.id == reservation_id).first()
#     if reservation:
#         reservation.payment_status = "Paid"
#         db.session.commit()
#         flash("Payment confirmed!")
#     return redirect(url_for("booking"))

@app.route('/to_book')
def to_book():
    pass

# @app.route("/delayed")
# def delayed():
#     if "Delayed" in session:
#         delayed_tours = session["Delayed"]
#         delayed_tours["total"] = 0
#         for tour_id in delayed_tours["items"]:
#             tour = Tours.query.filter(Tours.id == int(tour_id)).first()
#             delayed_tours["items"][tour_id]["item"] = tour.name
#             delayed_tours["items"][tour_id]["price"] = tour.price * delayed_tours["items"][tour_id]["qty"]
#             delayed_tours["total"] += delayed_tours["items"][tour_id]["price"]
#         return render_template("delayed.html", delayed_tours=delayed_tours)
#     return make_response("Delayed session not found", 404)


# @app.route("/remove_item/")
# def remove_from_delayed():
#     tour_id = request.args.get("tour_id")
#     item = session["Delayed"]["items"].pop(str(tour_id))
#     session.modified = True
#     return redirect("/delayed")

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