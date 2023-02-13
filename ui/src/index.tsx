import './index.css';

import React from 'react';
import ReactDOM from 'react-dom';
// import { Editor } from './components/Editor';
import { Editor } from "./components/Editor";

ReactDOM.render(
	<React.StrictMode>
		<Editor />
	</React.StrictMode>,
	// <React.StrictMode>
	// 	<App />
	// </React.StrictMode>,
	document.getElementById('root'),
);
