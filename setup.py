#!/usr/bin/env python
from setuptools import setup

setup(
    name="django-plop",
    version="0.0.1",

    packages=["django-plop"],
    install_requires = [
        'Django>=1.0',
        'plop==0.1.1',
    ],

    author="Brian Hicks",
    url="https://github.com/brianhicks/django-plop",
    description="Middleware for Django to support plop profiling",
    long_description=open("README.md").read(),
)
