```python
from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import BadSignature, SignatureExpired
from src.models.user import User
from src.utils.database import db
from src.config import SECRET_KEY

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user and check_password_hash(user.password, data['password']):
        s = Serializer(SECRET_KEY, expires_in=3600)
        return jsonify({'message': 'AUTH_SUCCESS', 'token': s.dumps({'id': user.id}).decode()})
    return jsonify({'message': 'AUTH_FAILURE'}), 401

@auth.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(username=data['username'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'USER_CREATED'}), 201
```