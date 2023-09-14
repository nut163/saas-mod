```python
from src.models.notification import Notification
from src.utils.database import db_session

NOTIFICATION_CREATED = "Notification created successfully."
NOTIFICATION_UPDATED = "Notification updated successfully."
NOTIFICATION_DELETED = "Notification deleted successfully."

def createNotification(data):
    notification = Notification(**data)
    db_session.add(notification)
    db_session.commit()
    return {"message": NOTIFICATION_CREATED, "notification": notification.to_dict()}

def updateNotification(notification_id, data):
    notification = Notification.query.get(notification_id)
    if not notification:
        return {"error": "Notification not found."}, 404
    notification.update(**data)
    db_session.commit()
    return {"message": NOTIFICATION_UPDATED, "notification": notification.to_dict()}

def deleteNotification(notification_id):
    notification = Notification.query.get(notification_id)
    if not notification:
        return {"error": "Notification not found."}, 404
    db_session.delete(notification)
    db_session.commit()
    return {"message": NOTIFICATION_DELETED}
```