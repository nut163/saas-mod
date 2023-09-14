```python
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'
    DATABASE_URI = os.environ.get('DATABASE_URI') or 'your-database-uri'
```