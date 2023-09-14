import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Product = () => {
    const [products, setProducts] = useState([]);

    useEffect(() => {
        fetchProducts();
    }, []);

    const fetchProducts = async () => {
        try {
            const response = await axios.get('/api/products');
            setProducts(response.data);
        } catch (error) {
            console.error('Error fetching products', error);
        }
    };

    return (
        <div id="productListing">
            <h2>Products</h2>
            {products.map(product => (
                <div key={product.id}>
                    <h3>{product.name}</h3>
                    <p>{product.description}</p>
                    <p>Price: {product.price}</p>
                </div>
            ))}
        </div>
    );
};

export default Product;