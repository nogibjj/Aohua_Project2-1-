#!/usr/bin/env python

import click
from dblib.querydb import querydb, findsalary

# build a click group
@click.group()
def cli():
    """A simple CLI to query a SQL database"""


# build a click command
@cli.command()
@click.option(
    "--query",
    default="SELECT * FROM default.ds_salaries_csv LIMIT 2",
    help="SQL query to execute",
)
def cli_query(query):
    """Execute a SQL query"""
    querydb(query)

@cli.command()
@click.option(
    "--level",
    default="EN",
    help="SQL query to execute",
)
@click.option(
    "--number",
    default=10,
    help="SQL query to execute",
)
def findsalarybylevel(level, number):
    """input a level of ds engineer, find the most salary(in usd) in this level"""
    findsalary(level, number)


# run the CLI
if __name__ == "__main__":
    cli.add_command(cli_query)
    cli.add_command(findsalarybylevel)
    cli()
