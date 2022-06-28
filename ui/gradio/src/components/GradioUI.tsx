import React from 'react';
import { useNavigate } from "react-router-dom";

import { useLightningState } from "/home/krshrimali/Documents/Projects/Lightning-AI/lightning-apps/LAI-CodeRunner-App/ui/src/hooks/useLightningState";


export const GradioUI: React.FC = () => {
	// const divEl = useRef<HTMLDivElement>(null);
	// const { lightningState } = useLightningState();

	// let host = "";
	// let port = 0;
	// let url: string = "http://" + host + ":" + String(port);
	let url: string = "http://127.0.0.1:9000";
	let navigate = useNavigate();

	// function getURL() {
	// 	if (lightningState) {
	// 		url = lightningState.flows.code_editor.works.gradio_image.url;
	// 	}
	// }

	// getURL();

	// useEffect(() => {
	// 	if (divEl.current) {
	// 		// just store the URL of Gradio App
	// 		host = "127.0.0.1";
	// 		port = 8080;
	// 		url = "https://" + host + ":" + String(port);
	// 	}
	// })

	// <!-- ref={divEl} -->


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
