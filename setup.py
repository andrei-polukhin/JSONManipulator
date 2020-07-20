#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""
from setuptools import setup, find_packages

with open("README.rst", 'r') as file:
    readme = file.read()

with open("HISTORY.rst", 'r') as hist:
    history = hist.read()

long_description = readme + "\n\n" + history


setup(
    name="JSONManipulator",
    description="A Python package to manipulate objects in JSON files.",
    url="https://github.com/pandrey2003/JSONManipulator",
    version="3.0.1",
    long_description=long_description,
    author="Andrew Polukhin",
    author_email="andrewmathematics2003@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English'
    ],
    keywords="Python JSON Objects",
    python_requires="~=3.6",
    packages=find_packages()
)
