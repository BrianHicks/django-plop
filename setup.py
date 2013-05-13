#!/usr/bin/env python
from setuptools import setup

setup(
    name="django_plop",
    version="0.0.1",

    packages=["django_plop"],
    install_requires = [
        'Django>=1.0',
        'plop==0.1.1',
    ],
    extras_require = {
        'viewer': 'tornado==3.0.1',
    },
    classifiers = [
        "Development Status :: 4 - Beta",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 2.7",
        #"Programming Language :: Python :: 3.3", # update when Django does
    ],

    author="Brian Hicks",
    author_email="brian@brianthicks.com",
    url="https://github.com/brianhicks/django-plop",
    description="Middleware for Django to support plop profiling",
    long_description=open("README.rst").read(),
)
