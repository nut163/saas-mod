import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Notification = () => {
    const [notifications, setNotifications] = useState([]);

    useEffect(() => {
        fetchNotifications();
    }, []);

    const fetchNotifications = async () => {
        try {
            const response = await axios.get('/api/notifications');
            setNotifications(response.data);
        } catch (error) {
            console.error('Error fetching notifications:', error);
        }
    };

    return (
        <div id="notificationListing">
            <h2>Notifications</h2>
            {notifications.length > 0 ? (
                <ul>
                    {notifications.map((notification) => (
                        <li key={notification.id}>
                            <h3>{notification.title}</h3>
                            <p>{notification.message}</p>
                        </li>
                    ))}
                </ul>
            ) : (
                <p>No notifications at this time.</p>
            )}
        </div>
    );
};

export default Notification;