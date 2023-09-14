```python
import unittest
from src.services.order_service import OrderService

class TestOrderService(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.order_service = OrderService()

    def test_create_order(self):
        order_data = {
            'user_id': 1,
            'product_id': 1,
            'quantity': 2
        }
        response = self.order_service.createOrder(order_data)
        self.assertEqual(response, 'ORDER_CREATED')

    def test_update_order(self):
        order_data = {
            'order_id': 1,
            'user_id': 1,
            'product_id': 2,
            'quantity': 3
        }
        response = self.order_service.updateOrder(order_data)
        self.assertEqual(response, 'ORDER_UPDATED')

    def test_delete_order(self):
        order_id = 1
        response = self.order_service.deleteOrder(order_id)
        self.assertEqual(response, 'ORDER_DELETED')

if __name__ == '__main__':
    unittest.main()
```