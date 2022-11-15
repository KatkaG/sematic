# Third party
import pytest

# Sematic
from sematic.types.types.chip import Chip


def test_label_pass():
    chip = Chip(label="enum1", variant="filled", size="medium")
    assert chip.label == "enum1"
    assert chip.variant == "filled"
    assert chip.size == "medium"


def test_label_fail():
    with pytest.raises(ValueError, match="Incorrect value for label"):
        Chip(label="", variant="filled", size="medium")


def test_variant():
    chip = Chip(label="enum1", size="medium")
    assert chip.label == "enum1"
    assert chip.variant == "filled"
    assert chip.size == "medium"


def text_size():
    chip = Chip(label="enum1")
    assert chip.label == "enum1"
    assert chip.variant == "filled"
    assert chip.size == "medium"
