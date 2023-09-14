import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Report = () => {
    const [reports, setReports] = useState([]);

    useEffect(() => {
        fetchReports();
    }, []);

    const fetchReports = async () => {
        try {
            const response = await axios.get('/api/reports');
            setReports(response.data);
        } catch (error) {
            console.error('Error fetching reports:', error);
        }
    };

    return (
        <div id="reportListing">
            <h2>Reports</h2>
            {reports.length > 0 ? (
                <ul>
                    {reports.map((report) => (
                        <li key={report.id}>
                            <h3>{report.title}</h3>
                            <p>{report.description}</p>
                        </li>
                    ))}
                </ul>
            ) : (
                <p>No reports available.</p>
            )}
        </div>
    );
};

export default Report;