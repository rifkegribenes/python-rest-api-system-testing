from models.user import UserModel
from tests.base_test import BaseTest


class UserTest(BaseTest):
    def test_create_user(self):
        user = UserModel('test', '1234')

        self.assertEqual(user.username, 'test',
                         "The username after creation does not equal the constructor argument.")
        self.assertEqual(user.password, '1234',
                         "The password after creation does not equal the constructor argument.")
