from typing import Optional, Union, Any
import ast

import cv2
import logging

from lightning.app.components.python.tracer import TracerPythonScript


class Visitor(ast.NodeTransformer):
    def __init__(self, expected):
        self.expected = expected
        self.found_it = False

    def visit_FunctionDef(self, node: ast.FunctionDef) -> Any:
        if node.name == self.expected:
            self.found_it = True


# class ASTChecker:
#     def __init__(self, script_path: str, expectations: str) -> None:
#         self.expectations = expectations
#         self.script_path = script_path
#         self.visitor = Visitor(self.expectations)
#         self.content = []

#     # @staticmethod
#     # def read_file(script_path):
#     #     lines = []
#     #     with open(script_path, 'r') as _file:
#     #         lines = _file.readlines()
#     #     return lines

#     def runme(self):
#         self.content = ASTChecker.read_file(self.script_path)
#         tree = ast.parse(''.join(self.content))
#         self.visitor.visit(tree)
#         return self.visitor.found_it


class PythonTracer(TracerPythonScript):
    def __init__(self, content, script_path: str, script_args: Optional[Union[list, str]] = None, expected_symbol: str = None, **kwargs):
        super().__init__(script_path, script_args, **kwargs)
        self.expected_symbol = expected_symbol
        self.script_content = content
        self.script_path = script_path
        self.output_path = script_path.strip(".py") + "_output.png"
        self.script_args = []

    def _read_file(self):
        lines = []
        with open(self.script_path, 'r') as _file:
            lines = _file.readlines()
        return lines

    def _ast_parse(self):
        tree = ast.parse(self.script_content)
        visitor = Visitor(self.expected_symbol)
        visitor.visit(tree)
        return visitor.found_it

    def _modify_script(self, img_path):
        content = self._read_file()
        append_sys = [
            # "import sys\n",
            "\nif __name__ == '__main__':\n",
            f"    img = cv2.imread('{img_path}')\n",
            "    output_img = input_frame(img)\n"
        ]
        content.extend(append_sys)
        with open(self.script_path, "w+") as _file:
            _file.write(self.script_content + '\n')
            for line in content:
                _file.write(line)

    # def run(self, drive, script_path, img):
    def run(self, content, script_path, img):
        with open(script_path, "w+") as _file:
            _file.write(content + '\n')
        self.script_content = content
        self.script_path = script_path
        self.output_path = self.script_path.strip(".py") + "_output.png"
        # drive.get(self.script_path)
        # ast_checker = ASTChecker(content, self.script_path, expectations=self.expected_symbol)
        # was_found = ast_checker.runme()
        was_found = self._ast_parse()
        if not was_found:
            raise ValueError(f"Expected a function with name {self.expected_symbol} in the given code at {self.script_path}")
        else:
            # Modify the script here and then run!!
            img_path = "from_numpy.jpg"
            cv2.imwrite(img_path, img)
            self._modify_script(img_path)
            super().run()

    def on_after_run(self, res: Any):
        output_img = res["output_img"]
        # TODO: Should this happen in the script itself? [can't access drive then, maybe? or can get the output path from res]
        cv2.imwrite(self.output_path, output_img)