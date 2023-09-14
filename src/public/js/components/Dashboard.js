import React, { Component } from 'react';
import axios from 'axios';

class Dashboard extends Component {
    constructor(props) {
        super(props);
        this.state = {
            user: {},
            products: [],
            orders: [],
            invoices: [],
            reports: [],
            notifications: [],
        };
    }

    componentDidMount() {
        this.getUserData();
        this.getProducts();
        this.getOrders();
        this.getInvoices();
        this.getReports();
        this.getNotifications();
    }

    getUserData() {
        axios.get('/api/user')
            .then(response => {
                this.setState({ user: response.data });
            })
            .catch(error => {
                console.error(error);
            });
    }

    getProducts() {
        axios.get('/api/products')
            .then(response => {
                this.setState({ products: response.data });
            })
            .catch(error => {
                console.error(error);
            });
    }

    getOrders() {
        axios.get('/api/orders')
            .then(response => {
                this.setState({ orders: response.data });
            })
            .catch(error => {
                console.error(error);
            });
    }

    getInvoices() {
        axios.get('/api/invoices')
            .then(response => {
                this.setState({ invoices: response.data });
            })
            .catch(error => {
                console.error(error);
            });
    }

    getReports() {
        axios.get('/api/reports')
            .then(response => {
                this.setState({ reports: response.data });
            })
            .catch(error => {
                console.error(error);
            });
    }

    getNotifications() {
        axios.get('/api/notifications')
            .then(response => {
                this.setState({ notifications: response.data });
            })
            .catch(error => {
                console.error(error);
            });
    }

    render() {
        return (
            <div className="dashboard">
                <h1>Welcome, {this.state.user.name}</h1>
                <div className="dashboard-content">
                    <div className="products">
                        {/* Render products here */}
                    </div>
                    <div className="orders">
                        {/* Render orders here */}
                    </div>
                    <div className="invoices">
                        {/* Render invoices here */}
                    </div>
                    <div className="reports">
                        {/* Render reports here */}
                    </div>
                    <div className="notifications">
                        {/* Render notifications here */}
                    </div>
                </div>
            </div>
        );
    }
}

export default Dashboard;