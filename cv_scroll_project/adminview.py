import flask_admin as fladmin
import flask_login as login
from flask import redirect, url_for
from flask_admin import helpers, expose
from models import User
from flask_admin.contrib.sqla import ModelView


class MyAdminIndexView(fladmin.AdminIndexView):
    """
    Overriding of Admin index view
    """

    @expose('/')
    def index(self):
        """
        Authorization for '/admin' panel
        :return: redirect to '/login' if user not logged in or his role not Admin
        """
        if not login.current_user.is_authenticated:  # если пользователь не авторизован то сразу переадресовываем на логин
            return redirect(url_for('login'))
        else:
            admin = User.query.filter(User.id == login.current_user.get_id()).first()
            if admin.role == 1:  # проверяем роль текущего пользователя, если она админ отдаем страницу
                return super(MyAdminIndexView, self).index()
            else:
                return redirect(url_for('login'))


class MyModelView(ModelView):
    """
    Overriding of base ModelView to add authentication for other admin paths
    """
    column_hide_backrefs = False

    def is_accessible(self):
        """
        This method used to check is current user is authenticated and his role is Admin
        :return:
        """
        if not login.current_user.is_authenticated:
            return False
        else:
            admin = User.query.filter(User.id == login.current_user.get_id()).first()
            if admin.role == 1:
                return True
            return False
        
class ToursView(MyModelView):
    """
    View for '/admin/tours'
    """
    can_delete = False
    column_list = ("id", "name", "price", "reservation")  
    column_searchable_list = ["name", "price"] 
    column_sortable_list = ["name"]  


class ReservationView(MyModelView):
    """
    View for '/admin/reservations'
    """
    can_delete = False
    column_list = ("id", "tour_id", "user_id", "date", "status", "payment_status")  
    # column_searchable_list = ["date", "status", "payment_status"]  
    # column_sortable_list = ["date", "status", "payment_status"]
    column_searchable_list = ["tour_id", "user_id", "date", "status", "payment_status"]
    column_sortable_list = ["tour_id", "user_id", "date", "status", "payment_status"]




# 1. Статус бронирования ("status"):
#    - Pending (В ожидании): Новое бронирование, ожидающее подтверждения или обработки.
#    - Confirmed (Подтверждено): Бронирование успешно подтверждено и зарезервировано.
#    - Cancelled (Отменено): Бронирование было отменено по какой-либо причине.
#    - Completed (Завершено): Бронирование было успешно завершено, например, поездка или услуга состоялась.

# 2. Статус оплаты ("payment_status"):
#    - Unpaid (Не оплачено): Бронирование создано, но оплата еще не была совершена.
#    - Pending (В ожидании): Оплата находится в процессе обработки или ожидает подтверждения.
#    - Paid (Оплачено): Оплата была успешно совершена.
#    - Partially Paid (Частично оплачено): Была совершена частичная оплата, но полная сумма еще не оплачена.
#    - Refunded (Возвращено): Оплата была возвращена по какой-либо причине.