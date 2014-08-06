#!/usr/bin/env python
# coding: utf-8

"""
siskin is a set of tasks for library metadata management.
~~~~~~
"""

try:
    from setuptools import setup
except:
    from distutils.core import setup

setup(name='vupy',
      version='0.1.0',
      description='Python helper for Vufind.',
      url='https://github.com/ubleipzig/vupy',
      author='Leander Seige',
      author_email='seige@ub.uni-leipzig.de',
      scripts=[
        'bin/vufmdump',
      ],
      install_requires=[
        'solrpy==0.9.6',
      ],
)
