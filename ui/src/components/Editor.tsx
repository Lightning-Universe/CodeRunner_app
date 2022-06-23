import React, { useRef, useEffect, MouseEvent } from 'react';
import * as monaco from 'monaco-editor';

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

export const Editor: React.FC = () => {
	const divEl = useRef<HTMLDivElement>(null);
	const clickButton = useRef<HTMLButtonElement>(null);
	let editor: monaco.editor.IStandaloneCodeEditor;

	const handleClick = (e: MouseEvent<HTMLButtonElement>) => {
		const id = e.currentTarget.id;
		if (id == "submit_button") {
			let code = editor.getValue();
			const element = document.createElement("a");
			const file = new Blob([code], {type: 'text/plain'});
			element.href = URL.createObjectURL(file);
			element.download = "myFile.py";
			document.body.appendChild(element); // Required for this to work in FireFox
			element.click();
		}
	}

	useEffect(() => {
		if (divEl.current) {
			editor = monaco.editor.create(divEl.current, {
				// value: ['function x() {', '\tconsole.log("Hello world!");', '}'].join('\n'),
				value: ["def input(img):", "\t# Play with your image here", "\treturn img"].join("\n"),
				theme: 'vs-dark',
				language: 'python',
				automaticLayout: true,
			});
		}
		return () => {
			editor.dispose();
		};
	}, []);
	// if (document.getElementById("container")) {
	// 	document.getElementById("container").onclick = saveFile;
	// }
	return (
		<div>
			<div className="Editor" ref={divEl}></div>
			<button className="button hoverButton" type="button" id="submit_button" onClick={handleClick}>Submit Code</button>
		</div>
	);
};