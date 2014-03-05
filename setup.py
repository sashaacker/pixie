import os
import sys
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

install_requires = [
]

if sys.version_info[0:2] == (2, 6):
    pass

setup(
    name="pixie",
    author="Alexis Sasha Acker",
    author_email="asackerwalters@gmail.com",
    description="An IRC Bot",
    license="MIT",
    packages=find_packages(),
    long_description=read('README.rst'),
    install_requires=install_requires,
    setup_requires=['vcversioner'],
    vcversioner={
        'version_module_paths': ['pixie/_version.py'],
    },
)
