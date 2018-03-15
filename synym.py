import click
from thesaurus import Word

@click.command()
@click.version_option()
@click.argument('word')

def cli(word):
    rWord = Word(word)
    synonyms = rWord.synonyms()
    if not synonyms:
        click.echo("No results.")
        return

    for idx,synonym in enumerate(synonyms):
        click.echo("{0}. {1}".format(idx+1, synonym))
