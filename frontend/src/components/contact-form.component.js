import React, { Component } from 'react';

export default class ContactForm extends Component {
    constructor(props) {
        super(props);

        this.onChangeName = this.onChangeName.bind(this);
        this.onChangeEmail = this.onChangeEmail.bind(this);
        this.onChangeMessage = this.onChangeMessage.bind(this);
        this.onSubmit = this.onSubmit.bind(this);

        this.state = {
            name    : '',
            email   : '',
            message : ''
        }
    }

    
    componentDidMount() {
        // this gets called on start
    }

    onChangeName(e) {
        this.setState({
            name: e.target.value
        });
    }

    onChangeEmail(e) {
        this.setState({
            email: e.target.value
        });
    }

    onChangeMessage(e) {
        this.setState({
            message: e.target.value
        });
    }

    onSubmit(e) {
        e.preventDefault();

        const payload = {
            name    : this.state.name,
            email   : this.state.email,
            message : this.state.message
        }

        console.log(payload);

        // send request to Mail service?

        // refresh page or display something
    }

    render() {
        return (
            <div className="u-clearfix u-form-spacing-20 u-form-vertical u-inner-form">
                <form onSubmit={this.onSubmit}>
                    <div className="u-form-group u-form-name">
                        <input type="text" 
                        placeholder="Enter your Name" 
                        id="name-3b9a" 
                        name="name" 
                        className="u-border-2 u-border-black u-border-no-left u-border-no-right u-border-no-top u-input u-input-rectangle u-input-1" 
                        required
                        value={this.state.name}
                        onChange={this.onChangeName}
                        />
                    </div>
                    <div className="u-form-group u-form-email">
                        <input type="text" 
                        placeholder="Enter a valid email address" 
                        id="email-3b9a" 
                        name="email" 
                        className="u-border-2 u-border-black u-border-no-left u-border-no-right u-border-no-top u-input u-input-rectangle u-input-2" 
                        required
                        value={this.state.email}
                        onChange={this.onChangeEmail}
                        />
                    </div>
                    <div className="u-form-group u-form-message">
                        <textarea placeholder="Enter your message" 
                        rows="4" 
                        cols="50" 
                        id="message-3b9a" 
                        name="message" 
                        className="u-border-2 u-border-black u-border-no-left u-border-no-right u-border-no-top u-input u-input-rectangle u-input-3" 
                        required
                        value={this.state.message}
                        onChange={this.onChangeMessage}></textarea>
                    </div>
                    <div className="u-align-center u-form-group u-form-submit">
                        <input type="submit" value="Submit"/>
                    </div>
                </form>
            </div>
        )
    }
}