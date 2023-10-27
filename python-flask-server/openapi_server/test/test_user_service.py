from services.user_service import *
import unittest
from unittest.mock import patch

from openapi_server.models.user import User
from openapi_server.config_test import db
from openapi_server.service import UserService

class TestUserService(unittest.TestCase):
    def setUp(self):
        db.drop_all()
        db.create_all()
        self.user = User(username="testuser", password="testpassword")
        db.session.add(self.user)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_user(self):
        with patch.object(UserService, "create_user") as mock_create_user:
            mock_create_user.return_value = self.user
            user = UserService.create_user("testuser2", "testpassword2")
            self.assertEqual(user, self.user)

    def test_get_user_by_username(self):
        user = UserService.get_user_by_username("testuser")
        self.assertEqual(user, self.user)

    def test_get_user_by_username_none(self):
        user = UserService.get_user_by_username("nonexistentuser")
        self.assertIsNone(user)

if __name__ == "__main__":
    unittest.main()