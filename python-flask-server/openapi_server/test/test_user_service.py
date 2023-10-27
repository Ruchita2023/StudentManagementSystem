from services.user_service import *
import unittest
from openapi_server.models.user import User
from openapi_server.config_test import db
from openapi_server.services import UserService

class TestUserService(unittest.TestCase):
  
    def setUp(self):
        db.create_all()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_user(self):
        user = UserService.create_user('test_user', 'test_password')
        self.assertIsInstance(user, User)
        self.assertEqual(user.username, 'test_user')
        self.assertEqual(user.password, 'test_password')

    def test_get_user_by_username(self):
        user = UserService.create_user('test_user', 'test_password')
        retrieved_user = UserService.get_user_by_username('test_user')
        self.assertIsInstance(retrieved_user, User)
        self.assertEqual(retrieved_user.username, 'test_user')
        self.assertEqual(retrieved_user.password, 'test_password')

    def test_get_user_by_nonexistent_username(self):
        retrieved_user = UserService.get_user_by_username('nonexistent_user')
        self.assertIsNone(retrieved_user)

    def test_create_duplicate_user(self):
        user1 = UserService.create_user('test_user', 'test_password')
        with self.assertRaises(Exception):
            user2 = UserService.create_user('test_user', 'test_password')