## README for GitHub Bulk Clone

### Overview

**github-bulk-clone** is a Python package that allows you to efficiently clone all repositories from a specified GitHub user, including private ones if you have access.

### Installation

Install via pip:

```bash
pip install github-bulk-clone
```

### Usage

#### Command-line

Run the following command in your terminal:

```bash
python -m github_bulk_clone <username> <clone_directory> [-t <token>]
```

- `<username>`: GitHub username.
- `<clone_directory>`: Local directory for cloning.
- `-t <token>`: Optional GitHub personal access token.

Or you can just use `blkclone`

```bash
blkclone <username> <clone_directory> [-t <token>]
```

#### Python Script

Import and use the functions directly:

```python
from github_bulk_clone import clone_all_repos_of

clone_all_repos_of('USER_NAME', 'YOUR_TOKEN', './my_repos')
```

### Functions

- **`get_all_repo_names(api_token, username)`**: Fetches repository URLs.
- **`store_repo_names_to_file(repo_list, path)`**: Saves repository URLs to a file.
- **`clone_from_list(repos, clone_directory)`**: Clones repositories from a list.
- **`clone_all_repos_of(username, api_token, clone_directory)`**: Main function to clone repositories.

### License

This project is licensed under the MIT License.

### Contributing

Feel free to contribute via pull requests or by opening issues on GitHub.