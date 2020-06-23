# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='Shopping-Simple',
    version='0.1.0',
    description='Simple application to find sales based on criteria',
    long_description=readme,
    author='Francis Irizarry',
    author_email='Francis.X.Irizarry@gmail.com',
    url='https://github.com/Undid-Iridium/Shopping-Simple',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)