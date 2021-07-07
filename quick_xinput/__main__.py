import pydymenu
import argparse
import quick_xinput.xfuncs as xfuncs
from quick_xinput.console import console
from typing import Callable

parser = argparse.ArgumentParser(
    prog="python -m quick_xinput",
    description="Quickly turn on/off/toggle xinput devices.",
)
parser.add_argument(
    "action",
    help="are you enabling or disabling devices? (default: off)",
    choices=["on", "off", "toggle"],
    nargs="?",
    default="off",
)
group = parser.add_mutually_exclusive_group()
group.add_argument(
    "--fzf",
    "-f",
    help="Use terminal (fzf) to select -- DEFAULT",
    action="store_const",
    dest="mode",
    const="fzf",
)
group.add_argument(
    "--rofi",
    "-r",
    help="Use graphical interface (rofi) to select",
    action="store_const",
    dest="mode",
    const="rofi",
)
parser.set_defaults(mode="fzf", action="toggle")
args = parser.parse_args()
# console.log(args)


def choose_do(prompt: str, menu: Callable, action: Callable):
    sel = menu(xfuncs.xinputs(), prompt=prompt, multi=False)
    if sel is not None:
        # print(f"{sel = }")
        dev_id = xfuncs.get_device_id(sel[0])
        # console.log(f"{dev_id = }")
        state = "On" if action(dev_id) else "Off"
        console.print(f"Device {dev_id} turned {state}")


menu = pydymenu.fzf if args.mode == "fzf" else pydymenu.rofi
if args.action == "toggle":
    choose_do("Which device to TOGGLE? ", menu, xfuncs.toggle_device)
elif args.action == "on":
    choose_do("Which device to turn ON? ", menu, xfuncs.enable_device)
elif args.action == "off":
    choose_do("Which device to turn OFF? ", menu, xfuncs.disable_device)
