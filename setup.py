from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    package=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA examle python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/<username>/<package-name>',
    author="Daniel Sadeko",
    author_email='sadekodaniel@gmail.com'
)

