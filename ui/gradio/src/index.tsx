import './index.css';

// import React from 'react';
import { BrowserRouter } from "react-router-dom";
import ReactDOM from 'react-dom';
// import { useSlotProps } from '@mui/base';
import { GradioUI } from "./components/GradioUI";

ReactDOM.render(
	<BrowserRouter>
		<GradioUI />
	</BrowserRouter>,
	document.getElementById('root'),
);
