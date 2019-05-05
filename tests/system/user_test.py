from models.user import UserModel
from tests.base_test import BaseTest
import json


class UserTest(BaseTest):
    def test_register_user(self):
        with self.app() as c:
            with self.app_context():
                r = c.post('/register', data={'username': 'test', 'password': '1234'})

                self.assertEqual(r.status_code, 201)
                self.assertIsNotNone(UserModel.find_by_username('test'))
                self.assertDictEqual(d1={'message': 'User created successfully.'},
                                     d2=json.loads(r.data))

    def test_register_and_login(self):
        pass

    def test_register_duplicate_user(self):
        pass

