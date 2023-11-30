import unittest
from app import app, db
from models import *
from api_bp.api import *
from flask_testing import TestCase
app.secret_key = 'q942obV58YWNANSQAa3DvA'

class TestCase(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        self.app = app
        return self.app
    
    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_catalog(self):
        response = self.client.get('/catalog')
        self.assertEqual(response.status_code, 200)

    def test_contact(self):
        response = self.client.get('/contact')
        self.assertEqual(response.status_code, 200)

    def test_delayed(self):
        with self.client:
            with self.client.session_transaction() as sess:
                sess["Delayed"] = {'items': {1: {"item": "Tour 1", "qty": 2, "price": 100}}}
            response = self.client.get('/delayed')
            self.assertEqual(response.status_code, 200)

    def test_booking(self):
        with self.client:
            with self.client.session_transaction() as sess:
                sess["Booking"] = {'1': {'reservation_id': 3}}
                sess["Delayed"] = {'items': {'1': {'item': 'Горки Город', 'price': 2100.0, 'qty': 1}}}
            response = self.client.get('/booking')
            self.assertEqual(response.status_code, 200)

    def test_get_users(self):
        response = self.client.get('/api/get_users')
        self.assertEqual(response.status_code, 200)

    def test_get_user(self):
        user_id = User.query.first().id
        response = self.client.get(f'/api/get_user/{user_id}')
        self.assertEqual(response.status_code, 200)

    def test_get_roles(self):
        response = self.client.get('/api/get_roles')
        self.assertEqual(response.status_code, 200)

    def test_get_role(self):
        role_id = Roles.query.first().id
        response = self.client.get(f'/api/get_role/{role_id}')
        self.assertEqual(response.status_code, 200)    

    def test_get_tours(self):
        response = self.client.get('/api/get_tours')
        self.assertEqual(response.status_code, 200)

    def test_get_tour(self):
        tour_id = Tours.query.first().id
        response = self.client.get(f'/api/get_tour/{tour_id}')
        self.assertEqual(response.status_code, 200)

    def test_create_tour(self):
        new_tour = {"name": "Test Tour", "price": 100.0}
        response = self.client.post('/api/create_tour', json=new_tour)
        self.assertEqual(response.status_code, 201)

    def test_get_reservations(self):
        response = self.client.get('/api/get_reservations')
        self.assertEqual(response.status_code, 200)

    def test_get_reservation(self):
        reservation_id = Reservation.query.first().id
        response = self.client.get(f'/api/get_reservation/{reservation_id}')
        self.assertEqual(response.status_code, 200)

    def test_index(self):
        response = self.client.get('/')
        response = self.client.get('/index')
        response = self.client.get('/home')
        self.assertEqual(response.status_code, 200)

    def test_auth(self):
        self.app.post(
            '/login', data={'email': 'test@test.com', 'password': 'test'})
        response = self.client.get('/home')
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 200)

    def test_signup(self):
        response = self.client.get('/signup')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
