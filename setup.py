#!/usr/bin/env python
# coding: utf-8

"""
Python helper for vufind.
"""

try:
    from setuptools import setup
except:
    from distutils.core import setup

setup(name='vupy',
      version='0.1.1',
      description='Python helper for Vufind.',
      url='https://github.com/finc/vupy',
      author='Leander Seige',
      author_email='seige@ub.uni-leipzig.de',
      scripts=[
        'bin/vufmdump',
      ],
      install_requires=[
        'solrpy==0.9.6',
      ],
)
