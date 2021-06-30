#!/usr/bin/env python3
from setuptools import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup()
d['packages'] = ['hexapod_gazebo']
d['package_dir'] = {'': 'src'}

setup(**d)