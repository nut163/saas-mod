```python
import unittest
from src.services.product_service import ProductService
from src.models.product import Product

class TestProductService(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.product_service = ProductService()

    def test_create_product(self):
        product = Product(name="Test Product", price=100.0, description="Test Description")
        response = self.product_service.createProduct(product)
        self.assertEqual(response, "PRODUCT_CREATED")

    def test_update_product(self):
        product = Product(name="Updated Product", price=150.0, description="Updated Description")
        response = self.product_service.updateProduct(product)
        self.assertEqual(response, "PRODUCT_UPDATED")

    def test_delete_product(self):
        product_id = 1
        response = self.product_service.deleteProduct(product_id)
        self.assertEqual(response, "PRODUCT_DELETED")

if __name__ == '__main__':
    unittest.main()
```