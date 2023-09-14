```python
import unittest
from src.services.auth_service import authenticate

class TestAuthService(unittest.TestCase):

    def setUp(self):
        self.valid_credentials = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        self.invalid_credentials = {
            'username': 'invaliduser',
            'password': 'invalidpassword'
        }

    def test_authenticate_success(self):
        result = authenticate(self.valid_credentials['username'], self.valid_credentials['password'])
        self.assertEqual(result, 'AUTH_SUCCESS')

    def test_authenticate_failure(self):
        result = authenticate(self.invalid_credentials['username'], self.invalid_credentials['password'])
        self.assertEqual(result, 'AUTH_FAILURE')

if __name__ == '__main__':
    unittest.main()
```