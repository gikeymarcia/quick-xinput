import re
from subprocess import run

# from quick_xinput.console import console


def xinputs() -> list:
    xinput = run(["xinput", "list"], capture_output=True, text=True)
    if xinput.returncode == 0:
        lines = xinput.stdout.strip().split("\n")
        return lines
    else:
        raise OSError


def get_device_id(line_from_xin: str) -> int:
    """Take in a line of output from xinput list and return the device id."""
    pattern = r"id=([0-9]+).*$"
    if match := re.search(pattern, line_from_xin):
        device_id = match.groups()[0]
        return int(device_id)
    else:
        raise ValueError(
            "Could not find a valid device id within the provided string:\n"
            f"{line_from_xin}"
        )


def enable_device(dev_id: int) -> bool:
    """Take device id and return state after attempting to enable."""
    run(["xinput", "--enable", str(dev_id)])
    return device_state(dev_id)


def disable_device(dev_id: int) -> bool:
    """Take device id and return state after attempting to disable."""
    run(["xinput", "--disable", str(dev_id)])
    return device_state(dev_id)


def device_state(dev_id: int) -> bool:
    "Given device ID return True/False for Enabled/Disabled."
    props = run(["xinput", "--list-props", str(dev_id)], capture_output=True, text=True)
    for line in props.stdout.split("\n"):
        if "Enabled" in line:
            if match := re.search(r"^.*:.*([01]).*$", line):
                state = int(match.groups()[0])
                return False if state == 0 else True
    else:
        raise LookupError(f"Could not determine state for device {dev_id}")


def toggle_device(dev_id: int) -> bool:
    """Take a device id and toggle it On/Off

    Returns bool representing device state after toggle
    True = Enabled
    False = Disabled
    """
    toggle = disable_device if device_state(dev_id) == True else enable_device
    toggle(dev_id)
    return device_state(dev_id)
