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
        "peewee",
        "pywildcard",
    ],
)

# setup(
#     *, 
#     name: str=..., 
#     version: str=..., 
#     description: str=..., 
#     long_description: str=..., 
#     author: str=..., 
#     author_email: str=..., 
#     maintainer: str=..., 
#     maintainer_email: str=..., 
#     url: str=..., 
#     download_url: str=..., 
#     packages: List[str]=..., 
#     py_modules: List[str]=..., 
#     scripts: List[str]=..., 
#     ext_modules: List[Extension]=..., 
#     classifiers: List[str]=..., 
#     distclass: Type[Distribution]=..., 
#     script_name: str=..., 
#     script_args: List[str]=..., 
#     options: Mapping[str, Any]=..., 
#     license: str=..., 
#     keywords: Union[List[str], str]=..., 
#     platforms: Union[List[str], str]=..., 
#     cmdclass: Mapping[str, 
#     Type[Command]]=..., 
#     data_files: List[Tuple[str, List[str]]]=..., 
#     package_dir: Mapping[str, str]=..., 
#     obsoletes: List[str]=..., 
#     provides: List[str]=..., 
#     requires: List[str]=..., 
#     command_packages: List[str]=..., 
#     command_options: Mapping[str, Mapping[str, Tuple[Any, Any]]]=..., 
#     package_data: Mapping[str, List[str]]=..., 
#     include_package_data: bool=..., 
#     libraries: List[str]=..., headers: List[str]=..., 
#     ext_package: str=..., include_dirs: List[str]=..., 
#     password: str=..., fullname: str=..., 
#     **attrs: Any
#     )


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

