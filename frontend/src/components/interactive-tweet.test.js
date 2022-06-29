import React from 'react';
import renderer from 'react-test-renderer';

import InteractiveTweet from './interactive-tweet.component';

it('renders correctly', () => {
    
    const component = renderer.create(<InteractiveTweet />).toJSON();
    expect(component).toMatchSnapshot();   
});
