import os
from setuptools import setup

# Utility function to read the README file.
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = 'fgbuster',
    version = '0.0.1',
    author = 'Davide Poletti, Josquin Errard',
    author_email = 'davide.pole@gmail.com, josquin@apc.in2p3.fr',
    description = ('Handy parametric component separation tools'),
    license = 'MIT',
    keywords = 'statistics cosmology cmb foregrounds',
    url = 'https://github.com/fgbuster/fgbuster',
    packages = ['fgbuster'],
    long_description = read('README.md'),
    classifiers = ['Development Status :: 1 - Pre-Alpha'],
    test_suite = 'fgbuster.test'
)
