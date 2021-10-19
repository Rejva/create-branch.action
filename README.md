# Create branch action

Simple GitHub action to create a branch. Defaults to creating a new branch with
the same commit as the one that triggers the action, but this can also be
customized.

## Inputs

-   `github-token` (required): The GitHub token that will be used to access the
    GitHub API. This cannot be set by default, and you must explicitly pass
    this value (see usage below).
-   `branch-name` (required): Name of the branch to be created.

## Environment variables

-   `GITHUB_REPOSITORY`: Defaults to the current repository, but can be set to
    add a branch to a different repository on GitHub (with the appropriate
    access token).
-   `GITHUB_SHA`: The sha that specific which specific commit is used to create
    the branch. Defaults to the current commit, but can be set to use
    a different commit.

## Example usage

```
uses: Rejva/create-branch.action@v1
with:
  github-token: ${{ secrets.GITHUB_TOKEN }}
  branch-name: '<branch name>'
```
