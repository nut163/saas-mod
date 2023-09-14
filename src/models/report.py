```python
from sqlalchemy import Column, Integer, String, DateTime
from .database import Base

class Report(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    created_by = Column(Integer)
    updated_by = Column(Integer)
```