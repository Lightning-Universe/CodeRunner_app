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
        # self.script_drive = Drive("lit://script", allow_duplicates=True)
        self.script_path = None
        # self.drive = Drive("lit://HelloReact", allow_duplicates=True)
        self.generate_script_from_code()
        self.script_path = None

    def generate_script_from_code(self):
        file_id = int(random.random() * 100)
        self.script_path = f"script_{file_id}.py"
        with open(self.script_path, "a") as _file:
            _file.write(self.code + '\n')
        # self.drive.put(self.script_path)

    def run(self):
        if self.script_path is None:
            self.generate_script_from_code()

        if self.code == "":
            return

    def clear(self):
        # Clear all the script_path, code variables
        self.code = ""
        self.script_path = None

    def configure_layout(self):
        # if self.gradio_image.ready:
        #     # return [{"name": "Gradio", "content": self.gradio_image}]
        #     with open("log.txt", "w+") as _file:
        #         _file.write("Done\n\nbooo")
        # else:
        return StaticWebFrontend(Path(__file__).parent / "ui/dist")


class GradioFlow(L.LightningFlow):
    def __init__(self):
        super().__init__()
        self._gradio_work = GradioImage()

    def run(self, script_path, script_content):
        # self._gradio_work = gradio_img
        self._gradio_work.run(script_path, script_content)

    def configure_layout(self):
        return StaticWebFrontend(Path(__file__).parent / "ui/gradio/dist")


class HelloLitReact(L.LightningFlow):
    def __init__(self):
        super().__init__()
        self.code_editor = YourComponent()
        # self.gradio_flow = GradioFlow()

    def run(self):
        if self.code_editor.code != "":
            self.code_editor.run()
            # self.gradio_flow.run(self.code_editor.script_path, self.code_editor.code)
            self.code_editor.clear()

    def configure_layout(self):
        return [
            {"name": "React UI", "content": self.code_editor},
            # {"name": "Gradio Demo", "content": self.gradio_flow}
        ]


app = L.LightningApp(HelloLitReact())
