```python
import unittest
from services.invoice_service import InvoiceService

class TestInvoiceService(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.invoice_service = InvoiceService()

    def test_create_invoice(self):
        invoice = {
            'invoice_id': 'INV123',
            'order_id': 'ORD123',
            'user_id': 'USR123',
            'total_amount': 100.00,
            'status': 'Pending'
        }
        response = self.invoice_service.createInvoice(invoice)
        self.assertEqual(response, 'INVOICE_CREATED')

    def test_update_invoice(self):
        invoice = {
            'invoice_id': 'INV123',
            'status': 'Paid'
        }
        response = self.invoice_service.updateInvoice(invoice)
        self.assertEqual(response, 'INVOICE_UPDATED')

    def test_delete_invoice(self):
        invoice_id = 'INV123'
        response = self.invoice_service.deleteInvoice(invoice_id)
        self.assertEqual(response, 'INVOICE_DELETED')

if __name__ == '__main__':
    unittest.main()
```