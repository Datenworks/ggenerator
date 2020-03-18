import os

from setuptools import setup, find_packages


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
    version="0.1",
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
    ],
    entry_points="""
        [console_scripts]
        ggenerator=main:run
    """,
    )
