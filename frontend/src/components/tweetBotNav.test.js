import React from 'react';
import { render, unmountComponentAtNode } from "react-dom";
import { act } from "react-dom/test-utils";
import { fireEvent } from "@testing-library/react"

import TweetBotNav from './tweetBotNav.component';

let container = null;
let component = null;
beforeEach(() => {
  // setup a DOM element as a render target
  container = document.createElement("div");
  document.body.appendChild(container);
});

afterEach(() => {
  // cleanup on exiting
  unmountComponentAtNode(container);
  container.remove();
  container = null;
});

describe('Navbar Testing', () => {

    it('renders correctly on start', () => {
        act(() => {
            render(<TweetBotNav/>, container);
        });
        expect(container).toMatchSnapshot();
    });

    it('Can Switch between Search Functions', () => {
        act(() => {
            component = render(<TweetBotNav/>, container);
        });

        expect(component.state.function).toEqual("Tweet");
        expect(container.querySelector("div div select").value).toEqual("Tweet");

        component.onChangeSearchFunction({
            target: {
                name: "Testing",
                value: "Hashtag"
            }
        });

        expect(component.state.function).toEqual("Hashtag");
        expect(container.querySelector("div div select").value).toEqual("Hashtag")

        component.onChangeSearchFunction({
            target: {
                name: "Testing",
                value: "Account"
            }
        });

        expect(component.state.function).toEqual("Account");
        expect(container.querySelector("div div select").value).toEqual("Account")

        component.onChangeSearchFunction({
            target: {
                name: "Testing",
                value: "Tweet"
            }
        });

        expect(component.state.function).toEqual("Tweet");
        expect(container.querySelector("div div select").value).toEqual("Tweet")
    });

    it('Can handle input changes', () => {
        const mockEvent = {
            target: {
                name: "Testing",
                value: "This is a test"
            }
        }

        act(() => {
            component = render(<TweetBotNav/>, container);
        });

        expect(component.state.input).toEqual("");
        expect(container.querySelector("div div input").value).toEqual("");

        component.onChangeInput(mockEvent);

        expect(component.state.input).toEqual(mockEvent.target.value);
        expect(container.querySelector("div div input").value).toEqual(mockEvent.target.value);
    });
})