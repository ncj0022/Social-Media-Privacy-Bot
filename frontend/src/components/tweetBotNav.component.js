import React, { Component } from 'react';
import axios from 'axios';

import TweetResults from './tweet-results.component';

export default class TweetBotNav extends Component {
    constructor(props) {
        super(props);

        this.onChangeInput = this.onChangeInput.bind(this); // bind 'this' to its respective function
        this.onChangeSearchFunction = this.onChangeSearchFunction.bind(this);
        this.onSubmit = this.onSubmit.bind(this);
        this.handleKeyDown = this.handleKeyDown.bind(this);

        this.state = {
            input: '',
            function: "Tweet",
            output: {
                type: "Empty",
                tweet: "1234",
                label: 0,
                confidence: 1
            }            
        }
    }

    // this gets called on start
    componentDidMount() {

    }

    onChangeInput(e) {
        this.setState({
            input: e.target.value
        });
    }

    handleKeyDown(e) {
        if(e.key === 'Enter') {
            switch (this.state.function) {
                default:
                case "Tweet": this.searchByURL();
                    break;
                case "Account": this.searchByAccount();
                    break;
                case "Hashtag": this.searchByHashtag();
                    break;
            }
        }
    }

    onChangeSearchFunction(e) {
        this.setState({
            function: e.target.value
        });
    }

    onSubmit(e) {
        e.preventDefault();
        switch (this.state.function) {
            default:
            case "Tweet": this.searchByURL();
                break;
            case "Account": this.searchByAccount();
                break;
            case "Hashtag": this.searchByHashtag();
                break;
        }
    }

    searchByURL() {
        // break apart URL
        const tweet_id = this.state.input.match(/status\/(\d+)$/); // regex is one or more digits at the end of the URL followed by status/

        if (tweet_id != null) {
            axios.get('http://localhost:5001/tweet_id/' + tweet_id[1])
                .then(res => {

                    this.setState({
                        output:{
                            type: this.state.function,
                            tweet: res.data.tweet,
                            label: res.data.prediction,
                            confidence: res.data.probability
                        }
                    });
                })
                .catch(err => this.setState({ input: 'Failed to Find Tweet' }));
        }
        else {
            this.setState({
                input: 'Invalid URL'
            })
        }
    }

    searchByAccount() {
        var account = this.state.input;
        if(this.state.input[0] == '@')
            account = this.state.input.slice(1);


        // send request to Twitter API
        axios.get('http://localhost:5001/username/' + account)
            .then(res => {
                
                this.setState({
                    output:{
                        type: this.state.function,
                        tweet: res.data.tweet,
                        label: res.data.prediction,
                        confidence: res.data.tweet_probability
                    }
                });
            })
            .catch(err => console.log("Cannot reach Twitter API: " + err));
    }

    searchByHashtag() {
        var hashtag = this.state.input;
        if(this.state.input[0] == '#')
            hashtag = this.state.input.slice(1);

        // send request to Twitter API
        axios.get('http://localhost:5001/hashtag/' + hashtag)
            .then(res => {
                
                this.setState({
                    output:{
                        type: this.state.function,
                        tweet: res.data.tweet,
                        label: res.data.prediction,
                        confidence: res.data.tweet_probability
                    }
                });
            })
            .catch(err => console.log("Cannot reach Twitter API: " + err));
    }

    render() {
        return (
            <div className="bg-dark">
                <nav className="navbar navbar-dark navbar-expand bg-dark navigation-clean">
                    <a className="navbar-brand" href="#"><i>PROgrammers</i></a>
                    <div className="container align-middle">
                        <input 
                        type="text"
                        className="form-control"
                        placeholder="Search..."
                        value={this.state.input}
                        onChange={this.onChangeInput}
                        onKeyDown={this.handleKeyDown}
                        />
                        <select className="custom-select"
                        onChange={this.onChangeSearchFunction}
                        value={this.state.function}>
                            <option value="Tweet">Search by Tweet</option>
                            <option value="Account">Search by Account</option>
                            <option value="Hashtag">Search by Hashtag</option>
                        </select>
                        <button 
                        className="btn btn-primary mx-2"
                        data-bss-hover-animate="pulse"
                        type="button"
                        onClick={this.onSubmit}
                        >Search!</button>
                    </div>
                </nav>
                <div>
                    <TweetResults results = {this.state.output} />
                </div>
            </div>
        )
    }
}