from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField, SubmitField
from flask_wtf.recaptcha.fields import RecaptchaField
from wtforms.validators import DataRequired, Length, NumberRange
class PaymentForm(FlaskForm):
    card_number = StringField('Номер карты', validators=[DataRequired(), Length(min=16, max=16)])
    card_holder = StringField('Имя владельца карты', validators=[DataRequired(), Length(max=50)])
    expiration_date = DateField('Срок действия', format='%Y-%m-%d')
    cvv = IntegerField('CVV-код', validators=[DataRequired(), NumberRange(min=100, max=999)])
    amount = IntegerField('Сумма оплаты', validators=[DataRequired(), NumberRange(min=0)])
    submit = SubmitField('Оплатить')