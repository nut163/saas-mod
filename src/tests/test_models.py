```python
import unittest
from src.models.user import User
from src.models.product import Product
from src.models.order import Order
from src.models.invoice import Invoice
from src.models.report import Report
from src.models.notification import Notification
from src.models.audit import Audit

class TestModels(unittest.TestCase):

    def setUp(self):
        self.user = User('test_user', 'test_password', 'test_role')
        self.product = Product('test_product', 'test_description', 100)
        self.order = Order('test_order', 'test_user', 'test_product', 1)
        self.invoice = Invoice('test_invoice', 'test_order', 100)
        self.report = Report('test_report', 'test_content')
        self.notification = Notification('test_notification', 'test_content')
        self.audit = Audit('test_audit', 'test_action', 'test_user')

    def test_user_model(self):
        self.assertEqual(self.user.username, 'test_user')
        self.assertEqual(self.user.password, 'test_password')
        self.assertEqual(self.user.role, 'test_role')

    def test_product_model(self):
        self.assertEqual(self.product.name, 'test_product')
        self.assertEqual(self.product.description, 'test_description')
        self.assertEqual(self.product.price, 100)

    def test_order_model(self):
        self.assertEqual(self.order.order_id, 'test_order')
        self.assertEqual(self.order.user_id, 'test_user')
        self.assertEqual(self.order.product_id, 'test_product')
        self.assertEqual(self.order.quantity, 1)

    def test_invoice_model(self):
        self.assertEqual(self.invoice.invoice_id, 'test_invoice')
        self.assertEqual(self.invoice.order_id, 'test_order')
        self.assertEqual(self.invoice.amount, 100)

    def test_report_model(self):
        self.assertEqual(self.report.report_id, 'test_report')
        self.assertEqual(self.report.content, 'test_content')

    def test_notification_model(self):
        self.assertEqual(self.notification.notification_id, 'test_notification')
        self.assertEqual(self.notification.content, 'test_content')

    def test_audit_model(self):
        self.assertEqual(self.audit.audit_id, 'test_audit')
        self.assertEqual(self.audit.action, 'test_action')
        self.assertEqual(self.audit.user_id, 'test_user')

if __name__ == '__main__':
    unittest.main()
```