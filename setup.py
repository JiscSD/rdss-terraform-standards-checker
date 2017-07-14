#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name='terrachecker',
    version='0.0.2',
    description='Terraform checker.',
    author='Mark Winterbottom',
    author_email='mark.winterbottom@jisc.ac.uk',
    url='https://github.com/JiscRDSS/rdss-terraform-standards-checker',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'terrachecker=terrachecker.terrachecker:main'
        ]
    },
    install_requires=[
        'pyhcl==0.3.5'
    ],
    data_files=[('LICENSE.txt')],
    license='Apache License 2.0'
)
