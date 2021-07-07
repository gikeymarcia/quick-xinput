import pytest

import quick_xinput
from quick_xinput import *
from quick_xinput.console import console

# from quick_xinput.console import console


def test_get_xinput_list():
    assert type(quick_xinput.xinputs()) is list


def test_parse_states():
    for line in quick_xinput.xinputs():
        id_num = get_device_id(line)
        assert type(id_num) is int


@pytest.mark.parametrize(
    "input_str",
    [
        "this is an invalid line",
        "this one is closer id= 12 more stuff",
    ],
)
def test_parse_error_on_no_match(input_str):
    with pytest.raises(ValueError) as except_info:
        get_device_id(input_str)
    assert except_info.type == ValueError


def test_read_device_state():
    assert device_state(15) == False


def test_set_device_state():
    enable_device(15)
    assert device_state(15) == True
    disable_device(15)
    assert device_state(15) == False


def test_toggle_device():
    assert enable_device(15) == True
    toggle_device(15)
    assert device_state(15) == False


def test_read_device_state_fails():
    with pytest.raises(LookupError) as except_info:
        device_state(100)
    assert except_info.type is LookupError
