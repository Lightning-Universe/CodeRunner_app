import lightning as L
from code_editor.python_tracer import PythonTracer

import gradio as gr
import cv2


class GradioImage(L.LightningWork):
    def __init__(self):
        super().__init__()
        self.ready = False
        self._script_drive = None
        self._script_path = None
        self._script_runner = None

    def run(self, script_drive, script_path):
        self._script_path = script_path
        self._script_drive = script_drive
        self._script_runner = PythonTracer(self._script_path, expected_symbol="input_frame")
        interface = gr.Interface(
            fn=self._apply,
            inputs=gr.inputs.Image(type="numpy"),
            outputs=gr.outputs.Image(type="numpy"),
        )
        self.ready = True
        interface.launch(
            server_name=self.host,
            server_port=self.port,
        )

    def _apply(self, img):
        self._script_runner.run(drive=self._script_drive, script_path=self._script_path, img=img)
        output_img = cv2.imread(self._script_runner.output_path)
        return output_img