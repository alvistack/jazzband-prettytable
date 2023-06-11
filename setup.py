# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='prettytable',
    version='3.7.0',
    description='A simple Python library for easily displaying tabular data in a visually appealing ASCII table format',
    author_email='Luke Maurits <luke@maurits.id.au>',
    maintainer='Jazzband',
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Text Processing',
        'Typing :: Typed',
    ],
    install_requires=[
        'importlib-metadata; python_version < "3.8"',
        'wcwidth',
    ],
    extras_require={
        'tests': [
            'pytest',
            'pytest-cov',
            'pytest-lazy-fixture',
        ],
    },
    package_dir={
        '': 'src',
    },
    packages=[
        'prettytable',
    ],
)
