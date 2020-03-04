import click
from src.generators.handler import GeneratorsHandler
from src.generators.dryrunhandler import DryRunHandler
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
@click.option("--dryrun", "dryrun_flag",
              is_flag=True, default=False,
              required=False,
              help="This generate a sample of 10 records by the spec")
def generate(spec_path, dryrun_flag):
    if dryrun_flag:
        generate_dryrun(spec_path)
    else:
        generate_datasets(spec_path)


def generate_datasets(spec_path):
    try:
        generator = \
            GeneratorsHandler(arguments={'config_file': spec_path})
        for dset_name, dset_format, dset_path in generator.generate():
            click.echo("| Finished!\n"
                       f"| Dataset name: {dset_name}\n"
                       f"| Dataset format: {dset_format}\n"
                       f"| Dataset path: {dset_path}\n")
    except Exception as err:
        click.echo(f"Error: {err}")


def generate_dryrun(spec_path):
    dryrun = DryRunHandler(arguments={'config_file': spec_path})
    dryrun.generate()
