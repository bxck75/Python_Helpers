# -*- coding: utf-8 -*-

# Learn more: https://github.com/bxck75

from setuptools import setup, find_packages

with open('README.rst') as f: readme = f.read()

with open('LICENSE') as f: license = f.read()

setup(
    name='Helpers',
    version='0.1.4',
    description='Helpers package for Me, myself and I',
    author='Boudewijn Kooy',
    author_email='goldenkooy@gmail.com',
    maintainer='K00B404',
    maintainer_email='koob404@gmail.com',
    long_description=readme,
    url='https://github.com/bxck75/Python_Helpers',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=[
        "google-api-python-client >= 1.2",
        "oauth2client >= 4.0.0",
        "PyYAML >= 3.0",
        "pydrive >= 1.3",
        "colorama",
        "icrawler",
        "dlib",
        "gputil",
        "psutil",
        "humanize",
        "preprocessing",
        "peewee",
        
    ],
)

# Example bellow

# from setuptools import setup

# setup(
#     name='PyDrive',
#     version='1.3.1',
#     author='JunYoung Gwak',
#     author_email='jgwak@dreamylab.com',
#     maintainer='Robin Nabel',
#     maintainer_email='rnabel@ucdavis.edu',
#     packages=['pydrive', 'pydrive.test'],
#     url='https://github.com/gsuitedevs/PyDrive',
#     license='LICENSE',
#     description='Google Drive API made easy.',
#     long_description='Read the README.rst',
#     install_requires=[
#         "google-api-python-client >= 1.2",
#         "oauth2client >= 4.0.0",
#         "PyYAML >= 3.0",
#     ],
# )

