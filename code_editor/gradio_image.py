import asyncio
import threading

import cv2
import gradio as gr
import lightning as L

from code_editor.python_tracer import PythonTracer
from code_editor.utils import OpenCVConfig


class GradioImage(L.LightningWork):
    def __init__(self):
        super().__init__(cloud_build_config=OpenCVConfig())
        self.ready = False
        self.script_path = None
        self._script_runner = None
        self.script_content = ""

    def run(self, script_path, script_content, start_gradio: bool = True):
        self.script_path = script_path
        self.script_content = script_content
        with open(self.script_path, "w+") as _file:
            _file.write(script_content + "\n")
        self._script_runner = PythonTracer(self.script_content, self.script_path, expected_symbol="input_frame")
        if start_gradio:
            interface = gr.Interface(
                fn=self._apply, inputs=gr.inputs.Image(type="numpy"), outputs=gr.outputs.Image(type="numpy")
            )
            loop = asyncio.new_event_loop()
            thr = threading.Thread(
                target=self.launch_interface,
                args=(
                    interface,
                    loop,
                ),
            )
            thr.start()
        self.ready = True

    def launch_interface(self, interface, loop):
        asyncio.set_event_loop(loop)
        interface.launch(
            server_name=self.host,
            server_port=self.port,
            enable_queue=False,
        )

    def _apply(self, img):
        # self._script_runner.run(drive=self.drive, script_path=self._script_path, img=img)
        self._script_runner.run(content=self.script_content, script_path=self.script_path, img=img)
        output_img = cv2.imread(self._script_runner.output_path)
        return output_img

    def close(self):
        gr.close_all()
