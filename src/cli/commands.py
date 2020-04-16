import click
from src.generators.handler import GeneratorsHandler
from src.generators.dryrunhandler import DryRunHandler
from src.cli.ascii_art import ASCII_ART
from src.generators.datatypes import Metadata
from tabulate import tabulate
from locale import getdefaultlocale
from src import utils
from os import getenv

VERSION = getenv("TRAVIS_TAG", "0.1")
default_locale = getdefaultlocale()[0]


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
                       f"| Dataset: {dset_path}\n")
    except Exception as err:
        click.echo(f"Error: {err}")


def generate_dryrun(spec_path):
    try:
        dryrun = DryRunHandler(arguments={'config_file': spec_path})
        dryrun.generate()
    except Exception as err:
        click.echo(f"Error: {err}")


@execute.command()
@click.option("--locale", "locale",
              type=click.STRING,
              required=False,
              default=default_locale)
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
              default=default_locale)
@click.option("--params", "params", multiple=True, required=False)
def sample(typename, locale, params):
    params = utils.args_to_kwargs(params=params, separator='=')
    metadata = Metadata(locale=locale)

    try:
        sample = metadata.sample(typename, **params)
        click.echo(f"Sample: {sample}")
    except Exception as err:
        click.echo(f"Error: {err}")


def get_uri(dataset_name, output_type):
    return click.prompt(f"Please, enter a valid URI of destination "
                        f"for the dataset: {dataset_name} "
                        f"and destination: {output_type}", type=str)
