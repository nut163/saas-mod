```python
from flask import Flask
from src.routes import set_up_routes
from src.utils.database import db
from src.config import DATABASE_URI

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    set_up_routes(app)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
```