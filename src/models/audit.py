```python
from sqlalchemy import Column, Integer, String, DateTime
from .database import Base

class Audit(Base):
    __tablename__ = "audits"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    action = Column(String)
    timestamp = Column(DateTime)
    details = Column(String)
```