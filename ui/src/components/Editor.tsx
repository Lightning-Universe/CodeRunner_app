import React, { useRef, useEffect, MouseEvent } from 'react';
import * as monaco from 'monaco-editor';
import cloneDeep from "lodash/cloneDeep";

import { useLightningState } from "/home/krshrimali/Documents/Projects/Lightning-AI/lightning-apps/LAI-CodeRunner-App/ui/src/hooks/useLightningState";


// @ts-ignore
self.MonacoEnvironment = {
	getWorkerUrl: function (_moduleId: any, label: string) {
		if (label === 'json') {
			return './json.worker.bundle.js';
		}
		if (label === 'css' || label === 'scss' || label === 'less') {
			return './css.worker.bundle.js';
		}
		if (label === 'html' || label === 'handlebars' || label === 'razor') {
			return './html.worker.bundle.js';
		}
		if (label === 'typescript' || label === 'javascript') {
			return './ts.worker.bundle.js';
		}
		return './editor.worker.bundle.js';
	}
};


let editor: monaco.editor.IStandaloneCodeEditor;

const handleClick = (e: MouseEvent<HTMLButtonElement>) => {
	HandleEvents(editor, e);
}

const HandleEvents = (editor: monaco.editor.IStandaloneCodeEditor, e: MouseEvent<HTMLButtonElement>) => {
	const { lightningState, updateLightningState } = useLightningState();
	const id = e.currentTarget.id;
	if (id == "submit_button") {
		let code = editor.getValue();
		console.log("Code before: " + code);

		/* Now update the var in lightning state */
		if (lightningState) {
			console.log("Code: " + code);
			const newLightningState = cloneDeep(lightningState);
			newLightningState.flows.code_editor.vars.code = code;
			updateLightningState(newLightningState);
		}

		const element = document.createElement("a");
		const file = new Blob([code], {type: 'text/plain'});
		element.href = URL.createObjectURL(file);
		element.download = "myFile.py";
		document.body.appendChild(element); // Required for this to work in FireFox
		element.click();
	}
}


export const Editor: React.FC = () => {
	const divEl = useRef<HTMLDivElement>(null);
	useEffect(() => {
		if (divEl.current) {
			editor = monaco.editor.create(divEl.current, {
				// value: ['function x() {', '\tconsole.log("Hello world!");', '}'].join('\n'),
				value: ["def input(img):", "\t# Play with your image here", "\treturn img"].join("\n"),
				theme: 'vs-dark',
				language: 'python',
				// scrollbar: {
				// 	alwaysConsumeMouseWheel: true,
				// },
			});
		}

		// const parent = placeholder.parentElement

		// window.addEventListener("resize", () => {
		// 	editor.layout({ width: 0, height: 0 })

		// 	window.requestAnimationFrame(() => {
		// 		const rect = parent.getBoundingClientRect()
		// 		editor.layout({ width: rect.width, height: rect.height })
		// 	})
		// })
		return () => {
			editor.dispose();
		};
	}, []);
	return (
		<div>
			<div className="Editor" ref={divEl}></div>
			<button className="button hoverButton" type="button" id="submit_button" onClick={handleClick}>Submit Code</button>
		</div>
	);
}


// export default App;