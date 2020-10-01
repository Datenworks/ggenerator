import os
from os import getenv

from setuptools import setup, find_packages

VERSION = getenv("TRAVIS_TAG", 'v0.0')


def get_version(version):
    if version[0] == 'v':
        return version[1:]
    if version[:4] == 'dev-':
        return version[4:]
    raise ValueError("Malformed tag version")


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="ggenerator",
    author="Datenworks",
    author_email="contato@datenworks.com",
    description=("A tool capable to generate fake data with a "
                 "given specification defined as a JSON DSL"),
    url="https://datenworks.com/",
    license='MIT',
    project_urls={
        "Source Code": "https://github.com/Datenworks/ggenerator"
    },
    py_modules=['main'],
    long_description=read("README.md"),
    version=get_version(VERSION),
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "python-dateutil>=2.8.1",
        "pandas>=1.0.1",
        "click>=7.1.1",
        "tabulate>=0.8.6",
        "requests>=2.23.0",
        "gcsfs>=0.6.0",
        "s3fs>=0.4.0",
        "faker>=4.0.1",
        "sqlalchemy>=1.3.16",
        "mysql-connector-python>=8.0.19",
        "alive-progress>=1.5.1",
        "azure-storage-blob>=12.3.0",
        "psycopg2-binary>=2.8.5"
    ],
    extras_require={
        "mysql": ['mysqlclient>=1.4.6']
    },
    entry_points="""
        [console_scripts]
        ggenerator=main:run
    """,
    )
