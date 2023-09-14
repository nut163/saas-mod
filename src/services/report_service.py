```python
from src.models.report import Report
from src.utils.database import db_session

REPORT_CREATED = "Report created successfully."
REPORT_UPDATED = "Report updated successfully."
REPORT_DELETED = "Report deleted successfully."

def createReport(data):
    new_report = Report(**data)
    db_session.add(new_report)
    db_session.commit()
    return {"message": REPORT_CREATED}, 201

def updateReport(report_id, data):
    report = Report.query.filter_by(id=report_id).first()
    if report:
        for key, value in data.items():
            setattr(report, key, value)
        db_session.commit()
        return {"message": REPORT_UPDATED}, 200
    else:
        return {"message": "Report not found"}, 404

def deleteReport(report_id):
    report = Report.query.filter_by(id=report_id).first()
    if report:
        db_session.delete(report)
        db_session.commit()
        return {"message": REPORT_DELETED}, 200
    else:
        return {"message": "Report not found"}, 404
```