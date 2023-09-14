```python
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    created_at = Column(DateTime, index=True)
    updated_at = Column(DateTime, index=True)

    orders = relationship("Order", back_populates="user")
    invoices = relationship("Invoice", back_populates="user")
    notifications = relationship("Notification", back_populates="user")
    audits = relationship("Audit", back_populates="user")
```