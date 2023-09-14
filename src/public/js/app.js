import React from 'react';
import ReactDOM from 'react-dom';
import Header from './components/Header';
import Footer from './components/Footer';
import Dashboard from './components/Dashboard';
import Login from './components/Login';
import Register from './components/Register';
import Profile from './components/Profile';
import Product from './components/Product';
import Order from './components/Order';
import Invoice from './components/Invoice';
import Report from './components/Report';
import Notification from './components/Notification';
import Error from './components/Error';
import Help from './components/Help';

class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            currentPage: 'Dashboard'
        };
    }

    navigateTo = (page) => {
        this.setState({ currentPage: page });
    }

    render() {
        let CurrentComponent;
        switch (this.state.currentPage) {
            case 'Dashboard':
                CurrentComponent = Dashboard;
                break;
            case 'Login':
                CurrentComponent = Login;
                break;
            case 'Register':
                CurrentComponent = Register;
                break;
            case 'Profile':
                CurrentComponent = Profile;
                break;
            case 'Product':
                CurrentComponent = Product;
                break;
            case 'Order':
                CurrentComponent = Order;
                break;
            case 'Invoice':
                CurrentComponent = Invoice;
                break;
            case 'Report':
                CurrentComponent = Report;
                break;
            case 'Notification':
                CurrentComponent = Notification;
                break;
            case 'Error':
                CurrentComponent = Error;
                break;
            case 'Help':
                CurrentComponent = Help;
                break;
            default:
                CurrentComponent = Dashboard;
        }

        return (
            <div>
                <Header navigateTo={this.navigateTo} />
                <CurrentComponent />
                <Footer />
            </div>
        );
    }
}

ReactDOM.render(<App />, document.getElementById('root'));