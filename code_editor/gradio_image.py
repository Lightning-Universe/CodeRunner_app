import lightning as L
from lightning.app.storage import Drive

import gradio as gr
import cv2

from code_editor.python_tracer import PythonTracer
from code_editor.utils import OpenCVConfig


class GradioImage(L.LightningWork):
    def __init__(self):
        super().__init__(cloud_build_config=OpenCVConfig())
        self.drive = Drive("lit://drive_1", allow_duplicates=True)
        self.ready = False
        self._script_path = None
        self._script_runner = None

    def run(self, script_path, script_content):
        self._script_path = script_path
        with open(self._script_path, "w+") as _file:
            _file.write(script_content + "\n")
        self.drive.put(self._script_path)
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
        self._script_runner.run(drive=self.drive, script_path=self._script_path, img=img)
        output_img = cv2.imread(self._script_runner.output_path)
        return output_img 