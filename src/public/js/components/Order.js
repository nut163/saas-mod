import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Order = () => {
    const [orders, setOrders] = useState([]);

    useEffect(() => {
        fetchOrders();
    }, []);

    const fetchOrders = async () => {
        try {
            const response = await axios.get('/api/orders');
            setOrders(response.data);
        } catch (error) {
            console.error('Error fetching orders:', error);
        }
    };

    return (
        <div id="orderListing">
            <h2>Orders</h2>
            {orders.length > 0 ? (
                <ul>
                    {orders.map((order) => (
                        <li key={order.id}>
                            <h3>{order.title}</h3>
                            <p>{order.description}</p>
                        </li>
                    ))}
                </ul>
            ) : (
                <p>No orders found</p>
            )}
        </div>
    );
};

export default Order;