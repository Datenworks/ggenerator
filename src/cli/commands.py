import click
from src.generators.handler import GeneratorsHandler
from src.generators.dryrunhandler import DryRunHandler
from src.cli.ascii_art import ASCII_ART
from src.generators.datatypes import Metadata
from tabulate import tabulate
from locale import getdefaultlocale

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


@execute.command()
@click.option("--locale", "locale",
              type=click.STRING,
              required=False,
              default=getdefaultlocale()[0])
def list_generators(locale):
    metadata = Metadata(locale=locale)
    infos = metadata.info()
    print_tabulate(dataframe=infos, headers=infos.columns,
                   tablefmt="fancy_grid")


def print_tabulate(dataframe, headers, tablefmt):
    click.echo(tabulate(dataframe, headers=headers, tablefmt=tablefmt))


@execute.command("generate-sample")
@click.option("--type", "typename", type=click.STRING, required=True)
@click.option("--locale", "locale", type=click.STRING, required=False,
              default=getdefaultlocale()[0])
def sample(typename, locale):
    metadata = Metadata(locale=locale)
    sample = metadata.sample(typename)
    click.echo(f"Sample: {sample}")


def get_uri(dataset_name, output_type):
    return click.prompt(f"Please, enter a valid URI of destination "
                        f"for the dataset: {dataset_name} "
                        f"and destination: {output_type}", type=str)
