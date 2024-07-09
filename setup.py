from setuptools import setup, find_packages
from setuptools.command.install import install as _install
import subprocess
import sys


class CustomInstallCommand(_install):
    """Customized setuptools install command - prints a friendly greeting."""
    def run(self):
        _install.run(self)
        subprocess.check_call([sys.executable, 'post_install.py'])

with open('requirements.txt') as f:
    content= f.readlines()
requirements= [x.strip() for x in content]

setup (name= 'mlna',
       version= '0.0.1',
       description= 'the multilingual network analysis package',
       install_requires= requirements,
       packages= find_packages()
       )
