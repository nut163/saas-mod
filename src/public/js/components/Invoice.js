import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Invoice = () => {
    const [invoices, setInvoices] = useState([]);

    useEffect(() => {
        fetchInvoices();
    }, []);

    const fetchInvoices = async () => {
        try {
            const response = await axios.get('/api/invoices');
            setInvoices(response.data);
        } catch (error) {
            console.error('Error fetching invoices:', error);
        }
    };

    return (
        <div id="invoiceListing">
            <h2>Invoices</h2>
            {invoices.length > 0 ? (
                <ul>
                    {invoices.map((invoice) => (
                        <li key={invoice.id}>
                            <h3>{invoice.title}</h3>
                            <p>{invoice.description}</p>
                        </li>
                    ))}
                </ul>
            ) : (
                <p>No invoices found.</p>
            )}
        </div>
    );
};

export default Invoice;