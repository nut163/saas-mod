```python
import unittest
from src.services.audit_service import AuditService
from src.models.audit import Audit

class TestAuditService(unittest.TestCase):

    def setUp(self):
        self.audit_service = AuditService()

    def test_create_audit(self):
        audit = Audit("AUDIT_CREATED", "Test audit created")
        result = self.audit_service.createAudit(audit)
        self.assertEqual(result.message, "AUDIT_CREATED")

    def test_update_audit(self):
        audit = Audit("AUDIT_UPDATED", "Test audit updated")
        result = self.audit_service.updateAudit(audit)
        self.assertEqual(result.message, "AUDIT_UPDATED")

    def test_delete_audit(self):
        audit = Audit("AUDIT_DELETED", "Test audit deleted")
        result = self.audit_service.deleteAudit(audit)
        self.assertEqual(result.message, "AUDIT_DELETED")

if __name__ == '__main__':
    unittest.main()
```