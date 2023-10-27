from services.user_service import *
import unittest
from openapi_server.models.user import User
from openapi_server.config_test import db
import logging

logging.basicConfig(level=logging.INFO)

class TestUserService(unittest.TestCase):

    def test_create_user(self):
        # Test creating a user
        user = UserService.create_user("test_user", "test_password")
        self.assertIsInstance(user, User)
        self.assertEqual(user.username, "test_user")
        self.assertEqual(user.password, "test_password")

    def test_get_user_by_username(self):
        # Test getting a user by username
        UserService.create_user("test_user", "test_password")
        user = UserService.get_user_by_username("test_user")
        self.assertIsInstance(user, User)
        self.assertEqual(user.username, "test_user")
        self.assertEqual(user.password, "test_password")

    def test_get_user_by_nonexistent_username(self):
        # Test getting a user by a nonexistent username
        user = UserService.get_user_by_username("nonexistent_user")
        self.assertIsNone(user)

    def test_create_duplicate_user(self):
        # Test creating a user with a duplicate username
        UserService.create_user("test_user", "test_password")
        with self.assertRaises(Exception):
            UserService.create_user("test_user", "test_password")

    def test_create_user_with_empty_username(self):
        # Test creating a user with an empty username
        with self.assertRaises(Exception):
            UserService.create_user("", "test_password")

    def test_create_user_with_empty_password(self):
        # Test creating a user with an empty password
        with self.assertRaises(Exception):
            UserService.create_user("test_user", "")

if __name__ == '__main__':
    unittest.main()