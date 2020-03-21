import 'core-js';

import React from 'react';
import {render} from 'react-dom';

import AppContainer from './containers/AppContainer';

const APP_ROOT_ID = 'application_root';

export function renderApp() {
    render(<AppContainer />, document.getElementById(APP_ROOT_ID));
}

renderApp()

