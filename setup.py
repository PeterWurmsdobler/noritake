import os
import string

from setuptools import find_packages, setup

NAME = "noritake"
__version__ = None

repository_dir = os.path.dirname(__file__)

with open(os.path.join(repository_dir, "src", NAME, "_version.py")) as fh:
    exec(fh.read())

with open(os.path.join(repository_dir, "README.md")) as fh:
    long_description = fh.read()

with open(os.path.join(repository_dir, "requirements.txt")) as fh:
    REQUIREMENTS = [line for line in fh.readlines() if line.startswith(tuple(list(string.ascii_letters)))]


setup(
    description="Noritake Display Driver",
    author="Peter Wurmsdobler",
    author_email="peter@wurmsdobler.org",
    url="http://eumeles.wurmsdobler.org/",
    include_package_data=True,
    install_requires=REQUIREMENTS,
    long_description=long_description,
    name=NAME,
    package_dir={"": "src"},
    packages=find_packages("src"),
    version=__version__,
)
