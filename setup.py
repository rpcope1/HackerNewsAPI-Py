from setuptools import setup
__author__ = 'Robert P. Cope'
__version__ = '0.1.0'
__license__ = 'LGPL v3'
__date__ = 'October 2014'

setup(name='HackerNewsAPI',
      author=__author__,
      version=__version__,
      packages=['HackerNewsAPI'],
      install_requires=['requests >=2.0.0'],
      license=__license__,
      keywords='ycombinator hacker news',
      url='https://github.com/rpcope1/HackerNewsAPI-Py',
      description='A Python wrapper for the Official Hacker News API')