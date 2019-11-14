import click

from app import app
from app.db_commands import create_table


@app.cli.command('create_table')
@click.argument('table_name')
def create_telegram_table(table_name):
    create_table(table_name)
