def get_version(package):
    if 'TRAVIS_TAG' in os.environ:
        import os
        return os.getenv("TRAVIS_TAG", 'v0.0')
    else:
        try:
            from importlib.metadata import version
            return version(package)
        except ModuleNotFoundError:
            import pkg_resources
            return pkg_resources.get_distribution(package).version
