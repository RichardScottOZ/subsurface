# -*- coding: utf 8 -*-
"""
Python installation file.
"""
from os import path
from setuptools import setup, find_packages
import re

this_directory = path.abspath(path.dirname(__file__))

verstr = '0.1.0'
VERSIONFILE = path.join(this_directory, "subsurface", "_version.py")
with open(VERSIONFILE, 'r', encoding='utf-8')as f:
    verstrline = f.read().strip()
    pattern = re.compile(r"__version__ = ['\"](.*)['\"]")
    mo = pattern.search(verstrline)
if mo:
    verstr = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))

DESCRIPTION_FILE = path.join(this_directory, 'README.md')
with open(DESCRIPTION_FILE, 'r', encoding='utf-8') as f:
    long_description = f.read()

REQUIREMENTS = ['numpy',
                ]

TEST_REQUIREMENTS = ['pytest',
                     ]

CLASSIFIERS = ['Development Status :: 3 - Alpha',
               'Intended Audience :: Science/Research',
               'Natural Language :: English',
               'License :: OSI Approved :: Apache Software License',
               'Operating System :: OS Independent',
               ]

setup(name='subsurface',
      version=verstr,
      packages=find_packages(exclude=('tests', 'docs')),
      description='Subsurface data types and utilities',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://softwareunderground.org',
      author='Software Underground',
      author_email='hello@softwareunderground.org',
      license='Apache 2',
      tests_require=TEST_REQUIREMENTS,
      install_requires=REQUIREMENTS,
      classifiers=CLASSIFIERS,
      zip_safe=False,
      )
