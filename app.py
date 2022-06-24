# example_app.py

from pathlib import Path

import lightning as L
from lightning.app.frontend import StaticWebFrontend


class YourComponent(L.LightningFlow):
    def __init__(self):
        super().__init__()
        self.message_to_print = "Hello World!"
        self.should_print = False
        self.code = ""

    def run(self):
        with open("output.txt", "a") as _file:
            _file.write(self.code + '\n')

    def configure_layout(self):
        return StaticWebFrontend(Path(__file__).parent / "ui/dist")


class HelloLitReact(L.LightningFlow):
    def __init__(self):
        super().__init__()
        self.counter = 0
        self.code_editor = YourComponent()

    def run(self):
        # if self.react_ui.should_print:
        #     print(f"{self.counter}: {self.react_ui.message_to_print}")
        #     self.counter += 1
        if self.code_editor.code != "":
            print(f"code: {self.code_editor.code}")

    def configure_layout(self):
        return [{"name": "React UI", "content": self.code_editor}]


app = L.LightningApp(HelloLitReact())
