import click

from create_branch import create_branch


@click.command()
@click.argument("github_token")
@click.argument("branch_name")
@click.option("--repository", envvar="GITHUB_REPOSITORY")
@click.option("--sha", envvar="GITHUB_SHA")
def main(github_token, branch_name, repository, sha):
    """Create a branch on GitHub with the given name"""
    create_branch(github_token, branch_name, repository, sha)
    click.echo(f"Successfully created branch {branch_name}")
