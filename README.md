# Quick Xinput

Does it drive you mad when you're living that keyboard-driven lifestyle in the 
terminal and your wrist grazes the touchpad and send you off into a different 
window or desktop?

If so, `quick_xinput` is the Python module you need in your life. Bring up a 
quick selector in the terminal, `fzf`, or with a GUI, `rofi` and select an 
xinput device to toggle on/off.

### Usage

```bash
# toggle a device using fzf
python -m quick_xinput
# toggle a device using rofi
python -m quick_xinput --rofi
# disable a device with rofi (good for keybindings)
python -m quick_xinput off --rofi
```
