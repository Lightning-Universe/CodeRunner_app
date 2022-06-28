import React from 'react';
import { useNavigate } from "react-router-dom";

import { useLightningState } from "../hooks/useLightningState";


export const GradioUI: React.FC = () => {
	const { lightningState } = useLightningState();

	let url: string = "";
	let navigate = useNavigate();

	function getURL() {
		if (lightningState) {
			console.log("URL is: ");
			console.log(lightningState.flows);
			console.log(lightningState.works.gradio_work.vars._url);
			url = lightningState.works.gradio_work.vars._url;
			console.log(url);
		}
	}

	getURL();

	return (
		<div>
			<div className="gradio_ui">
				<iframe src={url} height="400" width="800"/>
			</div>
			<button onClick={() => navigate(-1)}> Go Back </button>
		</div>
	);
}


// export default App;
