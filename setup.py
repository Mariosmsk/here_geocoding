#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['requests', 'pyproj', 'pandas', 'here_location_services', 'openpyxl']

test_requirements = []

setup(
    author="Marios S. Kyriakou",
    author_email='mariosmsk@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    description='The "here-geocoding" package is a Python library designed to streamline the process of converting '
                'addresses stored in an Excel (xlsx) file into latitude and longitude coordinates. It provides a '
                'convenient solution for geocoding large sets of addresses using the HERE geocoding service.',
    entry_points={
        'console_scripts': [
            'here_geocoding=here_geocoding.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='here_geocoding',
    name='here_geocoding',
    packages=find_packages(include=['here_geocoding', 'here_geocoding.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/Mariosmsk/here_geocoding',
    version='0.2.0',
    zip_safe=False,
)
