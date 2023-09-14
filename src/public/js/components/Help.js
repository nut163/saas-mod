import React from 'react';

class Help extends React.Component {
    render() {
        return (
            <div id="helpSection">
                <h2>Help and Documentation</h2>
                <p>Welcome to our Help section. Here you will find comprehensive documentation and FAQs to assist you in understanding the functionalities of our application.</p>
                <h3>Frequently Asked Questions</h3>
                <ul>
                    <li>
                        <h4>How do I create a new user?</h4>
                        <p>To create a new user, navigate to the 'Users' section and click on 'Add User'. Fill in the required details and click 'Submit'.</p>
                    </li>
                    <li>
                        <h4>How do I update a product?</h4>
                        <p>To update a product, navigate to the 'Products' section, find the product you want to update and click on 'Edit'. Make the necessary changes and click 'Submit'.</p>
                    </li>
                    <li>
                        <h4>How do I view my invoices?</h4>
                        <p>To view your invoices, navigate to the 'Invoices' section. Here you will find a list of all your invoices.</p>
                    </li>
                    <li>
                        <h4>What do I do if I encounter an error?</h4>
                        <p>If you encounter an error, please take a screenshot and send it to our support team along with a description of what you were doing when the error occurred.</p>
                    </li>
                </ul>
            </div>
        );
    }
}

export default Help;