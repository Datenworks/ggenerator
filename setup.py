from setuptools import setup, find_packages


setup(
    name="ggnerator",
    version="0.1",
    packages=find_packages(),
    include_packages_data=True,
    install_requires=[
        'Click',
        'pandas',
        'python-dateutil'
    ],
    entry_points="""
    [console_scripts]
    main
    """)
