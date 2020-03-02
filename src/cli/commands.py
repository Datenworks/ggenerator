import click
from src.generators.handler import GeneratorsHandler
from src.cli.ascii_art import ASCII_ART

VERSION = "0.1"


@click.group()
@click.version_option(version=VERSION)
def execute():
    click.echo(ASCII_ART)
    click.echo(f"version: {VERSION}")
    click.echo("-------------------")


@execute.command()
@click.option('-s', '--spec', 'spec_path',
              type=click.Path(exists=True,
                              resolve_path=True,
                              file_okay=True,
                              dir_okay=False),
              required=True)
def generate(spec_path):
    generator = \
        GeneratorsHandler(arguments={'config_file': spec_path})
    for dset_name, dset_format, dset_path in generator.generate():
        click.echo("| Finished!\n"
                   f"| Dataset name: {dset_name}\n"
                   f"| Dataset format: {dset_format}\n"
                   f"| Dataset path: {dset_path}\n")


def get_uri(dataset_name, output_type):
    return click.prompt(f"Please, enter a valid URI of destination "
                        f"for the dataset: {dataset_name} "
                        f"and destination: {output_type}", type=str)
