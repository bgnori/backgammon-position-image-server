#!/usr/bin/python
# -*- coding=utf8 -*-

from setuptools import setup, find_packages

name = "image-server"
version = '0.0.1'

setup(
  name=name,
  packages = find_packages('src'),
  package_dir = {'':'src'},
  install_requires=open('freeze.txt').readlines(),
  include_package_data=True,
  package_data = {
    '': ['memo.txt', 'readme.txt'],
  },
  entry_points = {
    'console_scripts' :[
      'imageserver= app:main',
    ],
  },
  author='Noriyuki Hosaka',
  author_email='bgnori@gmail.com',
  description='Local HTTP Proxy with prefetching etc. for Tumblr',
  license='Proprietary',
  keywords='backgammon, position, image',
  url='https://github.com/bgnori/backgammon-position-image-server',
)

