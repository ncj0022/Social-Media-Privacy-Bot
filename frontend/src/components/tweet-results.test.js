import React from 'react';
import { render, unmountComponentAtNode } from "react-dom";
import { act } from "react-dom/test-utils";

import TweetResults from './tweet-results.component';

let container = null;
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
describe('Tweet Results Testing', () =>{
    it("renders correctly given Empty input", () => {
        const emptyOutput = {
            type: "Empty",
            tweet: "1234",
            label: 0,
            confidence: 1
        }
    
        act(() => {
            render(<TweetResults results = {emptyOutput}/>, container);
        });
        expect(container).toMatchSnapshot();
    });
    
    it('renders correctly given HAM Tweet results', () => {
        const testOutput = {
            type: "Tweet",
            tweet: "1383923017923760131",
            label: 0,
            confidence: 1
        };
    
        act(() => {
            render(<TweetResults results = {testOutput} />, container);
        });
    
        expect(container.querySelector("[data-testid=opening]").textContent).toBe("This Tweet is...");
    
        expect(container.querySelector("[data-testid=score]").textContent).toBe("HAM!");
    
        expect(container.querySelector("[data-testid=confidence]").textContent).toBe(" Confidence: 100% ");
        
    });
    
    it('renders correctly given SPAM Tweet results', () => {
        const testOutput = {
            type: "Tweet",
            tweet: "1383923017923760131",
            label: 1,
            confidence: 0
        };
    
        act(() => {
            render(<TweetResults results = {testOutput} />, container);
        });
    
        expect(container.querySelector("[data-testid=opening]").textContent).toBe("This Tweet is...");
    
        expect(container.querySelector("[data-testid=score]").textContent).toBe("SPAM!");
    
        expect(container.querySelector("[data-testid=confidence]").textContent).toBe(" Confidence: 0% ");
        
    });
    
    it('renders correctly given Account results', () => {
        const testOutput = {
            type: "Account",
            tweet: "1383923017923760131",
            label: .5,
            confidence: .5
        };
    
        act(() => {
            render(<TweetResults results = {testOutput} />, container);
        });
    
        expect(container.querySelector("[data-testid=opening]").textContent).toBe("This Account is...");
    
        expect(container.querySelector("[data-testid=score]").textContent).toBe(" 50% spam! ");
    
        expect(container.querySelector("[data-testid=confidence]").textContent).toBe(" Confidence: 50% ");
        
    });
    
    it('renders correctly given Hashtag results', () => {
        const testOutput = {
            type: "Hashtag",
            tweet: "1383923017923760131",
            label: .25,
            confidence: .75
        };
    
        act(() => {
            render(<TweetResults results = {testOutput} />, container);
        });
    
        expect(container.querySelector("[data-testid=opening]").textContent).toBe("This Hashtag is...");
    
        expect(container.querySelector("[data-testid=score]").textContent).toBe(" 25% spam! ");
    
        expect(container.querySelector("[data-testid=confidence]").textContent).toBe(" Confidence: 75% ");
        
    });
})
