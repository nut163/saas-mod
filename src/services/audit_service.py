```python
from src.models.audit import Audit
from src.utils.database import db_session

AUDIT_CREATED = "Audit record created successfully."
AUDIT_UPDATED = "Audit record updated successfully."
AUDIT_DELETED = "Audit record deleted successfully."

def createAudit(audit_data):
    new_audit = Audit(**audit_data)
    db_session.add(new_audit)
    db_session.commit()
    return {"message": AUDIT_CREATED, "audit": new_audit.to_dict()}

def updateAudit(audit_id, audit_data):
    audit = Audit.query.get(audit_id)
    if not audit:
        return {"error": "Audit record not found."}, 404
    audit.update(**audit_data)
    db_session.commit()
    return {"message": AUDIT_UPDATED, "audit": audit.to_dict()}

def deleteAudit(audit_id):
    audit = Audit.query.get(audit_id)
    if not audit:
        return {"error": "Audit record not found."}, 404
    db_session.delete(audit)
    db_session.commit()
    return {"message": AUDIT_DELETED}
```