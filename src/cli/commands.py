import click


@click.command()
@click.version_option(version="0.0.1")
@click.option('-s', '--spec', 'spec_path',
              type=click.Path(exists=True,
                              resolve_path=True,
                              file_okay=True,
                              dir_okay=False),
              required=True, prompt=True)
@click.option('-d', '--dryrun', 'dryrun',
              is_flag=True, required=False)
def execute(spec_path, dryrun_flag):
    for generated_file in generate(spec_path):
        click.echo(f"Finished, Saved on path: {generated_file}")


def generate(filepath):
    # TODO
    yield
