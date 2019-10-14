from setuptools import setup

from onnx_cli import __version__

setup(
    name="onnx-cli",
    version = __version__,
    packages = ["onnx_cli"],
    entry_points = {
        "console_scripts": [
            "onnx = onnx_cli.__main__:main"
        ]
    })
