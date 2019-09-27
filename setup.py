# -*- coding: utf-8 -*-

# Learn more: https://github.com/bxck75

from setuptools import setup, find_packages

with open('README.rst') as f: readme = f.read()

with open('LICENSE') as f: license = f.read()

setup(
    name='Helpers',
    version='0.1.3',
    description='Helpers package for Me, myself and I',
    long_description=readme,
    author='Boudewijn Kooij',
    author_email='goldenkooy@gmail.com',
    url='https://github.com/bxck75/Python_Helpers',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

