# Python Project Template

Basic shell to begin a new project.

### Features

- `bump2version`
- `setup.py`

# Getting Going

1. Name your package; e.g., `agi`
2. Edit `setup.py` with `name=agi`
3. Rename `mv package/ agi/`
3. Rename `mv package/package.py agi/agi.py`
4. Update `.bumpversion.cfg`
    - rename `[bumpversion:file:package/__init__.py]` to 
      `[bumpversion:file:agi/__init__.py]`
