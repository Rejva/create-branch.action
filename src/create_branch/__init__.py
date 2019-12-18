from pkg_resources import DistributionNotFound, get_distribution

from github import Github

try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    # package is not installed
    pass


def create_branch(github_token, branch_name, repository, sha):
    """Create a branch on GitHub with the given name"""
    g = Github(github_token)
    repo = g.get_repo(repository)
    repo.create_git_ref(f"refs/heads/{branch_name}", sha)
