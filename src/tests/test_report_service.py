```python
import unittest
from src.services.report_service import ReportService
from src.models.report import Report

class TestReportService(unittest.TestCase):

    def setUp(self):
        self.report_service = ReportService()

    def test_create_report(self):
        report = Report("Test Report", "This is a test report")
        result = self.report_service.createReport(report)
        self.assertEqual(result, "REPORT_CREATED")

    def test_update_report(self):
        report = Report("Test Report", "This is a test report")
        self.report_service.createReport(report)
        report.description = "Updated description"
        result = self.report_service.updateReport(report)
        self.assertEqual(result, "REPORT_UPDATED")

    def test_delete_report(self):
        report = Report("Test Report", "This is a test report")
        self.report_service.createReport(report)
        result = self.report_service.deleteReport(report)
        self.assertEqual(result, "REPORT_DELETED")

if __name__ == '__main__':
    unittest.main()
```