#!/usr/bin/env python
from setuptools import setup, find_packages


setup(
    name="PyMIPS",
    license="MIT",
    version="1.0",
    description="A python MIPS interpreter",
    author="Ashton Walden & Jiman Kim",
    author_email="awalden@pugetsound.edu",
    package_dir={"": "src"},
    packages=find_packages(where="src", exclude=["tests"]),
    include_package_data=True,
    entry_points={"console_scripts": ["pymips = PyMIPS.__main__:main"]},
)
