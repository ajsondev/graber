from setuptools import setup, find_packages
import os

ROOT = os.path.dirname(os.path.realpath(__file__))


setup(
    name = 'graber',
    version = '0.0.1',
    description = 'Collection of scraping logic implemented with Grab'
    author = 'Gregory Petukhov',
    author_email = 'lorien@lorien.name',
    install_requires = ['grab', 'six']
    packages = find_packages(exclude=[]),
    license = "MIT",
    classifiers = (
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ),
)
