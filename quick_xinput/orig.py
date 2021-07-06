#!/usr/bin/env python3
# Mikey Garcia, @gikeymarcia
# dependencies: rofi
# pip dependencies: pydymenu
# https://www.addictivetips.com/ubuntu-linux-tips/disable-the-touchpad-on-linux/

import argparse
import pydymenu
import subprocess as sp
import re
from sys import exit as sys_exit


def parse_id(xinput_line):
    find_id = re.match(r"^.*id=([0-9]+).*$", xinput_line)
    if find_id is not None:
        return find_id.group(0), find_id.group(1)


def rofi_select(sel_list, prompt="Choose: "):
    "Takes a list and uses rofi to return a selection."
    pipe_delim = "|".join(sel_list)
    opts = sp.Popen(["printf", pipe_delim], stdin=sp.PIPE, stdout=sp.PIPE)
    rofi = sp.Popen(
        ["rofi", "-dmenu", "-i", "-sep", "|", "-p", prompt],
        stdin=opts.stdout,
        stdout=sp.PIPE,
    )
    out, _ = rofi.communicate()
    selection = out.decode("utf-8").strip()
    return None if selection == "" else selection


def pick_device(selector, select_prompt="Pick a device: "):
    xinput_list = sp.run(["xinput", "list"], capture_output=True, text=True)
    options = xinput_list.stdout.strip().split("\n")
    if selector == "rofi":
        dev_choice = rofi_select(options, select_prompt)
    else:
        dev_choice = pydymenu.fzf(options, multi=False, prompt=select_prompt)
    if dev_choice:
        return parse_id(dev_choice)
    else:
        sys_exit("No selection made. Terminating.")


def config_mode(operation_mode):
    # TODO: allower operation_mode == "toggle"
    # xinput --list-props 14 | grep Enabled | sed -E "s/^.*([01])$/\1/g"
    if operation_mode == "toggle":
        sys_exit("This functionality is not yet working.")
    prompt = f"Pick a device to turn {operation_mode}: "
    return (prompt, operation_mode)


def quick_toggle(operation_mode, interface_type):
    prompt, operation_mode = config_mode(operation_mode)
    dev_line, dev_id = pick_device(interface_type, prompt)
    dev_enable = "0" if operation_mode == "off" else "1"
    sp.run(["xinput", "set-prop", dev_id, "Device Enabled", dev_enable])
    print(f"Turning {operation_mode.upper()}: device {dev_id}.")
    # print(dev_line)
    # print(operation_mode, interface_type)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="quickly turn on/off xinput devices")
    parser.add_argument(
        "action",
        help="are you enabling or disabling devices? (default: off)",
        choices=["on", "off", "toggle"],
        nargs="?",
        default="off",
    )
    group2 = parser.add_mutually_exclusive_group()
    group2.add_argument(
        "--fzf",
        "-f",
        help="Use terminal (fzf) to select -- DEFAULT",
        action="store_const",
        dest="mode",
        const="fzf",
    )
    group2.add_argument(
        "--rofi",
        "-r",
        help="Use graphical interface (rofi) to select",
        action="store_const",
        dest="mode",
        const="rofi",
    )
    parser.set_defaults(mode="fzf", action="off")
    args = parser.parse_args()

    quick_toggle(args.action, args.mode)
