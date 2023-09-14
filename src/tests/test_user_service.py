```python
import unittest
from src.services.user_service import UserService
from src.models.user import User

class TestUserService(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.user_service = UserService()

    def test_create_user(self):
        user = User("test_user", "test_password", "test_email@test.com")
        response = self.user_service.createUser(user)
        self.assertEqual(response, USER_CREATED)

    def test_update_user(self):
        user = User("test_user", "new_test_password", "new_test_email@test.com")
        response = self.user_service.updateUser(user)
        self.assertEqual(response, USER_UPDATED)

    def test_delete_user(self):
        user = User("test_user", "test_password", "test_email@test.com")
        response = self.user_service.deleteUser(user)
        self.assertEqual(response, USER_DELETED)

if __name__ == '__main__':
    unittest.main()
```