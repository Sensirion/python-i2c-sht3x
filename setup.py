#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re

from setuptools import setup, find_packages

# Python versions this package is compatible with
python_requires = '>=3.6, <4'

# Packages that this package imports. List everything apart from standard lib packages.
install_requires = [
    'sensirion-i2c-driver>=1.0.0,<2.0',
    'sensirion-driver-adapters>=2.1.8,<3.0',
    'sensirion-driver-support-types>=1.1.0,<2.0',
    'sensirion-shdlc-sensorbridge~=0.1.1'
]

# Packages required for tests and docs
extras_require = {
    'test': [
        'flake8~=3.7.8',
        'pytest~=6.2.5',
        'pytest-cov~=3.0.0',
    ],
    'docs': [
        'click==8.0.4',
        'jinja2==3.0.1',
        'sphinx~=4.2.0',
        'sphinx-rtd-theme~=0.5.2',
    ]
}

# Read version number from version.py
version_line = open("sensirion_i2c_sht3x/version.py", "rt").read()
result = re.search(r"^version = ['\"]([^'\"]*)['\"]", version_line, re.M)
if result:
    version_string = result.group(1)
else:
    raise RuntimeError("Unable to find version string")

# Use README.rst and CHANGELOG.rst as package description
root_path = os.path.dirname(__file__)
long_description = open(os.path.join(root_path, 'README.md')).read()

setup(
    name='sensirion_i2c_sht3x',
    version=version_string,
    author='Sensirion',
    author_email='info@sensirion.com',
    description='I2C driver for the Sensirion SHT3X sensor family',
    license='BSD',
    keywords="""Sensirion SHT3X
        I2C
        SHT30A
        SHT30
        SHT31A
        SHT31
        SHT33
        SHT35A
        SHT35""",
    project_urls={
        "Documentation": "https://sensirion.github.io/python-i2c-sht3x",
        "Repository": "https://github.com/Sensirion/python-i2c-sht3x",
        "Changelog": "https://github.com/Sensirion/python-i2c-sht3x/blob/master/CHANGELOG.rst",
    },
    packages=find_packages(exclude=['tests', 'tests.*']),
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires=python_requires,
    install_requires=install_requires,
    extras_require=extras_require,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
