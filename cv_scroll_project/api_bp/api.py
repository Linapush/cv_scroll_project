from flask import Blueprint, jsonify, request, abort
from models import db, User, Roles, Tours, Reservation
import jwt
from datetime import datetime, timezone, timedelta
from functools import wraps
from .decorator import token_required, roles_required
from flask_login import login_required

api_bp = Blueprint("api", __name__, template_folder='templates', static_folder='static')

@api_bp.route('/')
def api_index():
    return jsonify({'status': 200})

@api_bp.route('/get_tours', methods=['GET'])
# @login_required
def get_tours():
    tours = Tours.query.all()
    tours_data = [{"id": tour.id, 
                   "name": tour.name, 
                   "price": tour.price} for tour in tours]
    return jsonify(tours_data)


@api_bp.route('/get_tour/<int:tour_id>', methods=['GET'])
# @login_required
def get_tour(tour_id):
    tour = Tours.query.get(tour_id)
    if tour:
        tour_data = {
            "id": tour.id,
            "name": tour.name,
            "price": tour.price
        }
        return jsonify(tour_data)
    else:
        return jsonify({"message": "Tour not found"}), 404
    

@api_bp.route('/create_tour', methods=['POST'])
# @login_required
def create_tour():
    data = request.get_json()
    new_tour = Tours(name=data['name'], price=data['price'])
    db.session.add(new_tour)
    db.session.commit()
    return jsonify({"message": "Tour created", "id": new_tour.id}), 201

@api_bp.route('/update_tour/<int:tour_id>', methods=['PUT'])
# @login_required
def update_tour(tour_id):
    tour = Tours.query.get_or_404(tour_id)
    data = request.get_json()
    tour.name = data['name']
    tour.price = data['price']
    db.session.commit()
    return jsonify({"message": "Tour updated"}), 200

@api_bp.route('/delete_tour/<int:tour_id>', methods=['DELETE'])
# @login_required
def delete_tour(tour_id):
    tour = Tours.query.get_or_404(tour_id)
    db.session.delete(tour)
    db.session.commit()
    return jsonify({"message": "Tour deleted"}), 200


@api_bp.route('/get_users', methods=['GET'])
# @login_required
def get_users():
    users = User.query.all()
    users_data = [{
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "role": user.role  
    } for user in users]
    return jsonify(users_data)

@api_bp.route('/get_user/<int:user_id>', methods=['GET'])
# @login_required
def get_user(user_id):
    user = User.query.get(user_id)
    if user:
        user_data = {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "role": user.role,
            "reservations": [reservation.id for reservation in user.reservations]
        }
        return jsonify(user_data)
    else:
        return jsonify({"message": "User not found"}), 404
  
@api_bp.route('/create_user', methods=['POST'])
# @login_required
def create_user():
    data = request.get_json()
    new_user = User(name=data['name'], email=data['email'], password=data['password'], role=data['role'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created", "id": new_user.id}), 201

@api_bp.route('/update_user/<int:user_id>', methods=['PUT'])
# @login_required
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    data = request.get_json()
    user.name = data['name']
    user.email = data['email']
    # не забудьте добавить шифрование пароля в реальном приложении
    user.password = data['password']
    db.session.commit()
    return jsonify({"message": "User updated"}), 200

@api_bp.route('/delete_user/<int:user_id>', methods=['DELETE'])
# @login_required
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted"}), 200

@api_bp.route('/get_roles', methods=['GET'])
# @login_required
# @roles_required('admin')
def get_roles():
    roles = Roles.query.all()
    roles_data = [{"id": role.id, "name": role.name} for role in roles]
    return jsonify(roles_data)

@api_bp.route('/get_role/<int:role_id>', methods=['GET'])
# @login_required
# @roles_required('admin')
def get_role(role_id):
    role = Roles.query.get(role_id)
    if role:
        role_data = {
            "id": role.id,
            "name": role.name,
            "users": [{"id": user.id, "name": user.name} for user in role.users]
        }
        return jsonify(role_data)
    else:
        return jsonify({"message": "Role not found"}), 404

    
@api_bp.route('/create_role', methods=['POST'])
# @login_required
# @roles_required('admin')  # предполагаем, что этот декоратор проверяет наличие роли 'admin'
def create_role():
    data = request.get_json()
    new_role = Roles(name=data['name'])
    db.session.add(new_role)
    db.session.commit()
    return jsonify({"message": "Role created", "id": new_role.id}), 201

@api_bp.route('/update_role/<int:role_id>', methods=['PUT'])
# @login_required
# @roles_required('admin')
def update_role(role_id):
    role = Roles.query.get_or_404(role_id)
    data = request.get_json()
    role.name = data['name']
    db.session.commit()
    return jsonify({"message": "Role updated"}), 200

@api_bp.route('/delete_role/<int:role_id>', methods=['DELETE'])
# @login_required
# @roles_required('admin')
def delete_role(role_id):
    role = Roles.query.get_or_404(role_id)
    db.session.delete(role)
    db.session.commit()
    return jsonify({"message": "Role deleted"}), 200

@api_bp.route('/get_reservations', methods=['GET'])
# @login_required
def get_reservations():
    reservations = Reservation.query.all()
    reservations_data = [{
        "id": reservation.id,
        "date": reservation.date,
        "status": reservation.status,
        "payment_status": reservation.payment_status,
        "tour_id": reservation.tour_id,
        "user_id": reservation.user_id
    } for reservation in reservations]
    return jsonify(reservations_data)

@api_bp.route('/get_reservation/<int:reservation_id>', methods=['GET'])
# @token_required
def get_reservation(reservation_id):
    reservation = Reservation.query.get(reservation_id)
    if reservation:
        reservation_data = {
            "id": reservation.id,
            "date": reservation.date,
            "status": reservation.status,
            "payment_status": reservation.payment_status,
            "tour": reservation.tour.name,
            "user": reservation.user_id
        }
        return jsonify(reservation_data)
    else:
        return jsonify({"message": "Reservation not found"}), 404
    

@api_bp.route('/create_reservation', methods=['POST'])
# @login_required
def create_reservation():
    data = request.get_json()
    new_reservation = Reservation(
        tour_id=data['tour_id'],
        user_id=data['user_id'],
        date=data['date'],
        status=data.get('status', 'pending'),  # Установка статуса ‘pending’, если он не предоставлен
        payment_status=data.get('payment_status', 'unpaid')  # Установка статуса оплаты ‘unpaid’ если он не предоставлен
    )
    db.session.add(new_reservation)
    db.session.commit()
    return jsonify({"message": "Reservation created", "id": new_reservation.id}), 201

@api_bp.route('/update_reservation/<int:reservation_id>', methods=['PUT'])
# @login_required
def update_reservation(reservation_id):
    reservation = Reservation.query.get_or_404(reservation_id)
    data = request.get_json()
    reservation.date = data.get('date', reservation.date)
    reservation.status = data.get('status', reservation.status)
    reservation.payment_status = data.get('payment_status', reservation.payment_status)
    db.session.commit()
    return jsonify({"message": "Reservation updated"}), 200

@api_bp.route('/delete_reservation/<int:reservation_id>', methods=['DELETE'])
# @login_required
def delete_reservation(reservation_id):
    reservation = Reservation.query.get_or_404(reservation_id)
    db.session.delete(reservation)
    db.session.commit()
    return jsonify({"message": "Reservation deleted"}), 200

@api_bp.route("/auth", methods=["POST"])
def auth():
    if request.method == 'POST':
        data = request.get_json()
        login = data.get("login")
        password = data.get('password')
        user = User.query.filter_by(name=login).first()
        if not user or not user.password == password:
            return jsonify({"message": "Invalid credentials"}), 401
        
        exp = datetime.now(tz=timezone.utc) + timedelta(hours=1)
        token = jwt.encode({"user_id": user.id, "exp": exp}, api_bp.config['SECRET_KEY'], algorithm='HS256')
        return jsonify({"token": token})
    else:
        return abort(405)

# # # POSTMAN agent, curl. 
# # # у нас пока приложение на localhostе

# # # думаем какие данные отдавать

# # # есть готовый модуль Flask RESTful
# # # (FASTAPI внутри Flask)

# # # REST - архитектура
# # # - когда приложение работает на RESTAPI
# # # отослать заголовки данные в body 

# # # можем сдлеать ручку (ручки)
