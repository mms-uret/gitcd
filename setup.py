#!/usr/bin/env python3

from setuptools import setup

setup(
    name='gitcd',
    version='1.5.5',
    description='Tool for continuous delivery using git',
    author='Claudio Walser',
    author_email='claudio.walser@srf.ch',
    url='https://github.com/claudio-walser/gitcd',
    packages=[
        '.',
        'gitcd',
        'gitcd.Cli',
        'gitcd.Config',
        'gitcd.Git',
        'gitcd.Git.Commands'
    ],
    install_requires=['pyyaml', 'argparse', 'argcomplete', 'requests'],
    entry_points={
        'console_scripts': [
            'git-cd = gitcd.__main__:main'
        ]
    }
)
