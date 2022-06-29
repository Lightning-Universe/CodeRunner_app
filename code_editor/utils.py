from typing import List

import lightning as L


class OpenCVConfig(L.BuildConfig):
    def build_commands(self) -> List[str]:
        return [
            "pip uninstall -y opencv-python",
            "pip uninstall -y opencv-python-headless",
            "pip install opencv-python-headless==4.5.5.64",
        ]