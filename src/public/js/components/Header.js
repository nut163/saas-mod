import React from 'react';

const Header = () => {
    return (
        <header>
            <nav>
                <ul>
                    <li><a href="/">Home</a></li>
                    <li><a href="/products">Products</a></li>
                    <li><a href="/orders">Orders</a></li>
                    <li><a href="/invoices">Invoices</a></li>
                    <li><a href="/reports">Reports</a></li>
                    <li><a href="/notifications">Notifications</a></li>
                    <li><a href="/help">Help</a></li>
                </ul>
            </nav>
        </header>
    );
}

export default Header;