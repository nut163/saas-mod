import React from 'react';

class Error extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            errorMessage: props.errorMessage
        };
    }

    componentDidUpdate(prevProps) {
        if (prevProps.errorMessage !== this.props.errorMessage) {
            this.setState({
                errorMessage: this.props.errorMessage
            });
        }
    }

    render() {
        return (
            <div id="errorDisplay" className="error-container">
                <h2>Error</h2>
                <p>{this.state.errorMessage}</p>
            </div>
        );
    }
}

export default Error;