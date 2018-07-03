#! -*- coding:utf-8 -*-

from setuptools import setup, find_packages

# get version data
with open("VERSION") as fo:
    version = fo.read()

setup(
     name='flask_fido',
     version=version,
     description='A Description to change',
     author='author',
     packages=find_packages(exclude=('tests')),
     entry_points={
         'console_scripts': ['flask_fido=flask_fido.cmdline:main']
     }
)
