# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='fss',
    version='0.1.0',
    description='Package for FSS altenative SDK',
    long_description=readme,
    author='Muzaffer Kahraman - Muzo',
    author_email='muzaffer.kahraman@outlook.com',
    url='https://github.com/muzafferkahraman',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)