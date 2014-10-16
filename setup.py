from setuptools import setup
from HackerNewsAPI import __version__, __author__, __license__

setup(name='HackerNewsAPI',
      author=__author__,
      version=__version__,
      packages=['HackerNewsAPI'],
      install_requires=['requests >=1.0.0'],
      license=__license__,
      keywords='ycombinator hacker news',
      url='https://github.com/rpcope1/HackerNewsAPI-Py',
      description='A Python wrapper for the Official Hacker News API')