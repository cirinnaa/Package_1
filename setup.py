from setuptools import setup, find_packages

setup(
    name='Package_1',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/cirinnaa/Package_1',
    author='Angelica Cirinna',
    author_email='angelica.cirinna@avon.com'
)