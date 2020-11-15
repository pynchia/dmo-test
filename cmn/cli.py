"""
The command line interface to the application
"""
import click
import logging

from cmn.main import main


logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.ERROR)


M_LIMIT = 10000

@click.command()
@click.option(
    "--size", "-s", default=M_LIMIT, help="The max value of the m range"
)
@click.option(
    "--verbose", "-v", is_flag=True, default=False, help="Log at debug level"
)
def cli(size, verbose):
    if verbose:
        log.setLevel(logging.DEBUG)
    main(size)


if __name__ == '__main__':
    cli()
