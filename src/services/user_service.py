```python
from flask import Blueprint, request
from src.models.user import User
from src.utils.database import db
from src.utils.security import hash_password, check_password

user_service = Blueprint('user_service', __name__)

@user_service.route('/user', methods=['POST'])
def createUser():
    data = request.get_json()
    hashed_password = hash_password(data['password'])
    new_user = User(username=data['username'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return {'message': 'USER_CREATED'}, 201

@user_service.route('/user/<int:user_id>', methods=['PUT'])
def updateUser(user_id):
    data = request.get_json()
    user = User.query.get(user_id)
    if user:
        user.username = data['username']
        if 'password' in data:
            user.password = hash_password(data['password'])
        db.session.commit()
        return {'message': 'USER_UPDATED'}, 200
    else:
        return {'message': 'USER_NOT_FOUND'}, 404

@user_service.route('/user/<int:user_id>', methods=['DELETE'])
def deleteUser(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return {'message': 'USER_DELETED'}, 200
    else:
        return {'message': 'USER_NOT_FOUND'}, 404
```