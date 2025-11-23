import os
import requests
import subprocess
import getpass

PROJECT_NAME = "github-bulk-clone"

def get_all_repo_names(api_token: str,username: str) -> list[str]:
    """
    :param api_token:
    :param username:
    :return: A list of all public repositories (and private if access is granted) of a user
    """
    url = f"https://api.github.com/users/{username}/repos"
    repos = []
    headers = {
        "Authorization": f"Bearer {api_token}",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    params = {'per_page': 100}
    page = 1
    while True:
        response = requests.get(url, headers=headers, params={**params, 'page': page})
        if response.status_code != 200:
            print(f"Error while trying to fetch headers... {response.status_code}")
            print(response.json())
            break
        data = response.json()
        if not data:
            break
        repos.extend(data)
        page += 1

    return [
        f"https://github.com/{username}/{repo['name']}" for repo in repos
    ]

def store_repo_names_to_file(repo_list: list[str], path: str):
    with open(path,"w") as f:
        f.write(
            "".join([f"{i}\n" for i in repo_list])
        )
        print(f"Successfully wrote repos to file: {path}")

def clone_from_list(repos: list[str],clone_directory: str):

    os.makedirs(clone_directory, exist_ok=True)
    os.chdir(clone_directory)

    total_repos = len(repos)

    progress_counter = 1

    for repo in repos:
        repo_name = repo.split("/")[-1]

        if not os.path.exists(repo_name):
            print(f'Downloading repository {repo_name} number {progress_counter}, total repos: {total_repos}')
            subprocess.run(['git', 'clone', '--depth', '1', f'{repo}'])
            progress_counter += 1
        else:
            print(f'Skipping {repo_name}: Folder already exists.')










if __name__ == "__main__":
    target_user = input("Enter github username to clone: ")
    token = getpass.getpass("Enter your github AUTH token: ")
    os.makedirs("./dump", exist_ok=True)
    os.makedirs("./dump/repos", exist_ok=True)

    print(f"Getting repo names for {target_user}")
    file = f"./dump/{target_user}.repos"
    repos = []
    if os.path.exists(file):
        print(f"Headers already fetched, fetching from file {file}")
        with open(file,"r") as f:
            repos = [i[:-1] for i in f.readlines()]
    else:
        repos = get_all_repo_names(token, target_user)
        store_repo_names_to_file(repos, file)

    clone_dir = "./dump/repos"

    print(f"Cloning all repos of user {target_user}")
    clone_from_list(repos,clone_dir)


