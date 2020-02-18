import click


@click.command()
@click.version_option(version="0.0.1")
@click.option('-f', '--file-path', 'filepath',
              type=click.Path(exists=True,
                              resolve_path=True,
                              file_okay=True,
                              dir_okay=False),
              required=True, prompt=True)
def execute(filepath):
    for generated_file in generate(filepath):
        click.echo(f"Finished, Saved on path: {generated_file}")


def generate(filepath):
    # TODO
    yield
