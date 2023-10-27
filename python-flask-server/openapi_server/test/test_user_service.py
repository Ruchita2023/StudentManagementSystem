from services.user_service import *
import unittest
from openapi_server.models.user import User
from openapi_server.config_test import db
from openapi_server.service import UserService

class TestUserService(unittest.TestCase):

    def test_create_user(self):
        """
        Test creating a new user
        """
        user = UserService.create_user('test_user', 'test_pass')
        self.assertIsInstance(user, User)
        self.assertEqual(user.username, 'test_user')
        self.assertEqual(user.password, 'test_pass')

    def test_get_user_by_username(self):
        """
        Test getting a user by their username
        """
        UserService.create_user('test_user', 'test_pass')
        user = UserService.get_user_by_username('test_user')
        self.assertIsInstance(user, User)
        self.assertEqual(user.username, 'test_user')
        self.assertEqual(user.password, 'test_pass')

    def test_get_user_by_invalid_username(self):
        """
        Test getting a user with an invalid username
        """
        user = UserService.get_user_by_username('invalid_username')
        self.assertIsNone(user)

if __name__ == '__main__':
    unittest.main()