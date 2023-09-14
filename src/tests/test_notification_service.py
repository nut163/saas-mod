```python
import unittest
from src.services.notification_service import NotificationService

class TestNotificationService(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.notification_service = NotificationService()

    def test_create_notification(self):
        result = self.notification_service.create_notification("Test notification")
        self.assertEqual(result, "NOTIFICATION_CREATED")

    def test_update_notification(self):
        result = self.notification_service.update_notification(1, "Updated notification")
        self.assertEqual(result, "NOTIFICATION_UPDATED")

    def test_delete_notification(self):
        result = self.notification_service.delete_notification(1)
        self.assertEqual(result, "NOTIFICATION_DELETED")

if __name__ == '__main__':
    unittest.main()
```