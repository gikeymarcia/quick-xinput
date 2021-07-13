# https://realpython.com/pypi-publish-python-package/#a-small-python-package
from pathlib import Path
from setuptools import setup, find_packages

README = (Path(__file__).parent / "README.md").read_text()


# https://setuptools.readthedocs.io/en/latest/setuptools.html#basic-use
setup(
    name="quick-xinput",
    version="0.1.1",
    description="Quick selector to enable/disable/toggle xinput devices",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/gikeymarcia/quick-xinput",
    author="Mikey Garcia",
    author_email="gikeymarcia@gmail.com",
    license="GPL-3.0",
    packages=find_packages(exclude="test"),
    install_requires=[],
)
