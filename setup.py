# https://realpython.com/pypi-publish-python-package/#a-small-python-package
from pathlib import Path
from setuptools import setup, find_packages

README = (Path(__file__).parent / "README.md").read_text()


# https://setuptools.readthedocs.io/en/latest/setuptools.html#basic-use
setup(
    name="package",
    version="0.1.0",
    description="Short description of the project",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/gikeymarcia/",
    author="Mikey Garcia",
    author_email="gikeymarcia@gmail.com",
    license="GPL-3.0-or-later",
    packages=find_packages(exclude="test"),
    install_requires=[],
)
