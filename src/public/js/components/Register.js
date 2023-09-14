import React, { useState } from 'react';
import axios from 'axios';

const Register = () => {
    const [formData, setFormData] = useState({
        username: '',
        password: '',
        email: '',
    });

    const { username, password, email } = formData;

    const onChange = e => setFormData({ ...formData, [e.target.name]: e.target.value });

    const onSubmit = async e => {
        e.preventDefault();
        const newUser = {
            username,
            password,
            email
        };
        try {
            const config = {
                headers: {
                    'Content-Type': 'application/json'
                }
            };
            const body = JSON.stringify(newUser);
            const res = await axios.post('/api/users', body, config);
            console.log(res.data);
        } catch (err) {
            console.error(err.response.data);
        }
    };

    return (
        <div>
            <h1>Register</h1>
            <form onSubmit={e => onSubmit(e)}>
                <div>
                    <input 
                        type="text" 
                        placeholder="Username" 
                        name="username" 
                        value={username} 
                        onChange={e => onChange(e)} 
                        required 
                    />
                </div>
                <div>
                    <input 
                        type="email" 
                        placeholder="Email" 
                        name="email" 
                        value={email} 
                        onChange={e => onChange(e)} 
                        required 
                    />
                </div>
                <div>
                    <input 
                        type="password" 
                        placeholder="Password" 
                        name="password" 
                        value={password} 
                        onChange={e => onChange(e)} 
                        minLength="6"
                    />
                </div>
                <input type="submit" value="Register" />
            </form>
        </div>
    );
};

export default Register;