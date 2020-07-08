#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script"""
from setuptools import setup, find_packages

with open("README.md", 'r') as file:
    long_description = file.read()

setup(
    name="JSONManipulator",
    description="A Python package to manipulate objects in JSON files.",
    version="1.0",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="Andrew Polukhin",
    author_email="andrewmathematics2003@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English'
    ],
    keywords="JSON Objects Manipulation Tool",
    python_requires="~=3.6",
    packages=find_packages()
)
