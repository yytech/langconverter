# coding: utf-8

import os
from setuptools import setup


here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='langconverter',
    version='1.0',
    description='Language codes converter',
    long_description=long_description,
    url='https://github.com/FuGangqiang/',
    author='FuGangqiang',
    author_email='fu_gangqiang@qq.com',
    keywords='nltk langid bing',
    license='MIT',

    py_modules=['langconverter'],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'License :: OSI Approved :: MIT License',
    ],
)
