```python
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    invoice_date = Column(DateTime)
    total_amount = Column(Integer)
    status = Column(String)

    order = relationship("Order", back_populates="invoices")

    def __repr__(self):
        return f"Invoice(id={self.id}, order_id={self.order_id}, invoice_date={self.invoice_date}, total_amount={self.total_amount}, status={self.status})"
```