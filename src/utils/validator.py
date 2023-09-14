```python
from marshmallow import Schema, fields, validate

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True, validate=validate.Length(min=1))
    password = fields.Str(required=True, validate=validate.Length(min=8))
    email = fields.Email(required=True)
    role = fields.Str(required=True)

class ProductSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1))
    description = fields.Str(required=True)
    price = fields.Float(required=True)

class OrderSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    product_id = fields.Int(required=True)
    quantity = fields.Int(required=True)

class InvoiceSchema(Schema):
    id = fields.Int(dump_only=True)
    order_id = fields.Int(required=True)
    total_amount = fields.Float(required=True)

class ReportSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    content = fields.Str(required=True)

class NotificationSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    message = fields.Str(required=True)

class AuditSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    action = fields.Str(required=True)
    timestamp = fields.DateTime(required=True)
```