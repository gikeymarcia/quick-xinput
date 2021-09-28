# Quick Xinput

Does it drive you mad when you're living that keyboard-driven terminal lifestyle 
and your wrist grazes the touchpad sending you off to a different window or 
desktop?

If so, `quick_xinput` is the Python module you need in your life. Bring up a 
quick selector in the terminal, `fzf`, or with a GUI, `rofi` and select an 
xinput device to toggle on/off.

### Installation

```bash
pip install --user quick-xinput
```

### Usage

```bash
# disable a device using fzf
python -m quick_xinput off
# toggle a device using rofi (good for keybindings)
python -m quick_xinput toggle --rofi
```

### Source of Truth

This project is available on [GitHub][github] and [GitLab][gitlab]. Each push to 
`master` automatically goes to both so choose whichever platform you prefer. All
releases are published to [PyPi][pypi].

[github]: <https://github.com/gikeymarcia/quick-xinput>
"Follow and Contribute on GitHub"
[gitlab]: <https://gitlab.com/gikeymarcia/quick-xinput>
"Follow and Contribute on GitLab"
[pypi]: <https://pypi.org/project/quick-xinput/>
"PyPi homepage for quick-xinput"
