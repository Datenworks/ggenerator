import click

@click.command()
@click.option("--file", help="The config file path")
@click.version_option(version="0.0.1")
@click.argument("conf")
def start(file, conf):
    click.echo(conf)
    with click.progressbar([1 for _ in range(5000000)], fill_char='█', empty_char='▁') as bar:
        for item in bar:
            pass


if __name__ == '__main__':
    start()