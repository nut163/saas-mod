```python
from sqlalchemy import Column, Integer, String, DateTime
from .database import Base

class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    title = Column(String)
    message = Column(String)
    timestamp = Column(DateTime)

    def __init__(self, user_id, title, message, timestamp):
        self.user_id = user_id
        self.title = title
        self.message = message
        self.timestamp = timestamp
```