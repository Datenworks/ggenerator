def get_version(package):
    try:
        from importlib.metadata import version
        return version('ggenerator')
    except ModuleNotFoundError as err:
        import pkg_resources
        return pkg_resources.get_distribution('ggenerator').version