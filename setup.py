# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "cybersource-rest-client-python"
VERSION = "0.0.34"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

setup(
    name=NAME,
    version=VERSION,
    description="SDK for the CyberSource REST API",
    author_email="developer@cybersource.com",
    url="https://github.com/CyberSource/cybersource-rest-client-python",
    keywords=["Payments API", "CyberSource"],
    install_requires=[
        "certifi==2021.5.30",
        "cffi==1.15.0",
        "chardet==4.0.0",
        "charset-normalizer==2.0.12",
        "crypto==1.4.1",
        "cryptography==3.3.2",
        "DateTime==4.4",
        "idna==2.10",
        "Naked==0.1.31",
        "pycparser==2.21",
        "pycryptodome==3.13.0",
        "PyJWT==1.7.1",
        "pyOpenSSL==19.1.0",
        "pytz==2020.1",
        "PyYAML==5.4.1",
        "requests==2.25.1",
        "shellescape==3.8.1",
        "six==1.15.0",
        "urllib3==1.26.6",
        "zope.interface==5.4.0",
    ],
    packages=find_packages(),
    include_package_data=True,
    long_description="CyberSource REST API",
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
