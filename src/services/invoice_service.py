```python
from src.models.invoice import Invoice
from src.utils.database import db_session

INVOICE_CREATED = "Invoice created successfully."
INVOICE_UPDATED = "Invoice updated successfully."
INVOICE_DELETED = "Invoice deleted successfully."

def createInvoice(invoice_data):
    invoice = Invoice(**invoice_data)
    db_session.add(invoice)
    db_session.commit()
    return {"message": INVOICE_CREATED, "invoice": invoice_data}

def updateInvoice(invoice_id, invoice_data):
    invoice = db_session.query(Invoice).filter(Invoice.id == invoice_id).first()
    if invoice:
        for key, value in invoice_data.items():
            setattr(invoice, key, value)
        db_session.commit()
        return {"message": INVOICE_UPDATED, "invoice": invoice_data}
    else:
        return {"message": "Invoice not found."}

def deleteInvoice(invoice_id):
    invoice = db_session.query(Invoice).filter(Invoice.id == invoice_id).first()
    if invoice:
        db_session.delete(invoice)
        db_session.commit()
        return {"message": INVOICE_DELETED}
    else:
        return {"message": "Invoice not found."}
```