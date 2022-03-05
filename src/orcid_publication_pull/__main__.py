"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """ORCiD Publication Pull Github Action."""


if __name__ == "__main__":
    main(prog_name="orcid-publication-pull")  # pragma: no cover
