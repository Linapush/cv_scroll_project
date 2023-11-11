# from flask import Blueprint, jsonify, current_app, request, abort #хранится состояние текущего приложения
# from models import User
# import jwt
# from datetime import datetime, timezone, timedelta
# # from .decorator import token_required


# api_bp = Blueprint("api", __name__, template_folder='templates', static_folder='static')

# # @api_bp.route('/')
# # def api_index():
# #     return jsonify ({'status', 200})

# # @api_bp.route('/get_tours')
# # @token_required
# # def token_required():
# #     products = products.query.all()
# #     result = {}
# #     for product in products:
# #         result[product.id] = {"name":product.name,
# #                               "price": product.price}
# #     return jsonify({"products": result})
    

# # @api_bp.route('get_user', methods=['GET']) # получим id пользователя
# # @token_required
# # def get_user():
# #     if request.method == 'POST':
# #         user = request.json.get('id')
# #         user = User.query.filter(User.id == user.id).first()
# #         result = {
# #             user.id:{
# #                 "name": user.name,
# #                 "email": user.email,
# #                 "role": user.role,
# #                 "orders": [order.id for order in user.orders]

# #             }
# #         }
# #     return jsonify(result)

# # # В этом коде создается эндпоинт "/auth" для аутентификации пользователей.
# # # отправляем логин и пароль в постмен в body, получаем token
# # @api_bp.route("/auth", methods=["GET", "POST"])
# # def auth():
# #     if request.method == 'POST':
# #         login = request.json.get("login")
# #         password = request.json.get('password')
# #         #expiration of token
# #         exp = datetime.now(tz=timezone.utc) + datetime.timedelta(hours=1)  #expiration of token
# #         token = jwt.encode(dict(login=login, password=password, exp=exp), current_app.secret_key, algorithms=['HS256']) # заинкодили token
# #         # вернем польз в виде словарика статус и токен
# #         return {'status': 'token successfully generateed', "token": token}
# #     # Если запрос приходит методом GET, возвращается ошибка 405 (Method Not Allowed), так как данный эндпоинт поддерживает только метод POST.
# #     return abort(405)
    

# # # POSTMAN agent, curl. 
# # # у нас пока приложение на localhostе

# # # думаем какие данные отдавать

# # # есть готовый модуль Flask RESTful
# # # (FASTAPI внутри Flask)

# # # REST - архитектура
# # # - когда приложение работает на RESTAPI
# # # отослать заголовки данные в body 

# # # можем сдлеать ручку (ручки)
