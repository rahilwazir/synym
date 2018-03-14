import click
from thesaurus import Word

@click.command()
@click.version_option()
@click.argument('word')

def cli(word):
    rWord = Word(word)
    click.echo(rWord.synonyms())
