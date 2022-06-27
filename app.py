import random

from pathlib import Path

import lightning as L
from lightning.app.frontend import StaticWebFrontend
from lightning.app.storage import Drive

from code_editor.gradio_image import GradioImage


class YourComponent(L.LightningFlow):
    def __init__(self):
        super().__init__()
        self.code = ""
        self.script_drive = Drive("lit://script", allow_duplicates=True)
        self.script_path = None
        self.generate_script_from_code()
        self.gradio_image = GradioImage()
        self.script_path = None

    def generate_script_from_code(self):
        file_id = int(random.random() * 100)
        self.script_path = f"script_{file_id}.py"
        with open(self.script_path, "a") as _file:
            _file.write(self.code + '\n')

    def run(self):
        if self.script_path is None:
            file_id = int(random.random() * 100)
            self.script_path = f"script_{file_id}.py"
            with open(self.script_path, "a") as _file:
                _file.write(self.code + '\n')

        if self.code == "":
            return
        self.gradio_image.run(self.script_drive, self.script_path)

    def clear(self):
        # Clear all the script_path, code variables
        self.code = ""
        self.script_path = None

    def configure_layout(self):
        if self.gradio_image.ready:
            return [{"name": "Gradio", "content": self.gradio_image}]
        else:
            return StaticWebFrontend(Path(__file__).parent / "ui/dist")


class HelloLitReact(L.LightningFlow):
    def __init__(self):
        super().__init__()
        self.counter = 0
        self.code_editor = YourComponent()

    def run(self):
        if self.code_editor.code != "":
            self.code_editor.run()
            self.code_editor.clear()

    def configure_layout(self):
        return [{"name": "React UI", "content": self.code_editor}]


app = L.LightningApp(HelloLitReact())
