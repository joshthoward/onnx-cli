import pytest

from onnx_cli import utils

@pytest.mark.parametrize("name, expected", [
    ("modelzoo/inception", ("modelzoo", "inception", "latest")),
    ("modelzoo/inception:v2", ("modelzoo", "inception", "v2")),
    ("http://modelzoo/inception", ("http://modelzoo", "inception", "latest")),
])
def test_parse_name(name, expected):
    assert(expected == utils.parse_name(name))
