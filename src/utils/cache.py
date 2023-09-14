```python
import time
from threading import Lock

class Cache:
    def __init__(self):
        self.cache = {}
        self.lock = Lock()

    def get(self, key):
        with self.lock:
            data = self.cache.get(key)
            if data:
                value, exp = data
                if time.time() - exp < 0:
                    return value
                else:
                    del self.cache[key]
                    return None
            else:
                return None

    def set(self, key, value, ttl=None):
        with self.lock:
            self.cache[key] = (value, time.time() + ttl if ttl else float('inf'))

    def delete(self, key):
        with self.lock:
            if key in self.cache:
                del self.cache[key]

cache = Cache()
```