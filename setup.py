from setuptools import find_packages, setup
setup(
    name='cloudConnect',
    packages=find_packages(include=['connector']),
    version='0.0.1',
    description='A package to connect retrieve the API credentials in SAP BTP',
    author='Joel Kischkel',
    author_email='joel.kischkel@syntax.com',
    license='MIT',
    install_requires=['requests', 'cfenv'],
)

