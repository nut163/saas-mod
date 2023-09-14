```python
from flask import Blueprint, request
from src.models.order import Order
from src.utils.database import db_session
from src.utils.security import authorize_request

order_service = Blueprint('order_service', __name__)

@order_service.route('/order', methods=['POST'])
@authorize_request
def create_order():
    data = request.get_json()
    new_order = Order(**data)
    db_session.add(new_order)
    db_session.commit()
    return {'message': 'ORDER_CREATED', 'order': new_order.to_dict()}, 201

@order_service.route('/order/<int:order_id>', methods=['PUT'])
@authorize_request
def update_order(order_id):
    data = request.get_json()
    order = Order.query.get(order_id)
    for key, value in data.items():
        setattr(order, key, value)
    db_session.commit()
    return {'message': 'ORDER_UPDATED', 'order': order.to_dict()}, 200

@order_service.route('/order/<int:order_id>', methods=['DELETE'])
@authorize_request
def delete_order(order_id):
    order = Order.query.get(order_id)
    db_session.delete(order)
    db_session.commit()
    return {'message': 'ORDER_DELETED'}, 200
```