```python
from src.models.product import Product
from src.utils.database import db_session

PRODUCT_CREATED = "Product created successfully."
PRODUCT_UPDATED = "Product updated successfully."
PRODUCT_DELETED = "Product deleted successfully."

def createProduct(data):
    new_product = Product(**data)
    db_session.add(new_product)
    db_session.commit()
    return {"message": PRODUCT_CREATED}, 201

def updateProduct(product_id, data):
    product = Product.query.filter(Product.id == product_id).first()
    if product:
        for key, value in data.items():
            setattr(product, key, value)
        db_session.commit()
        return {"message": PRODUCT_UPDATED}, 200
    else:
        return {"message": "Product not found"}, 404

def deleteProduct(product_id):
    product = Product.query.filter(Product.id == product_id).first()
    if product:
        db_session.delete(product)
        db_session.commit()
        return {"message": PRODUCT_DELETED}, 200
    else:
        return {"message": "Product not found"}, 404
```