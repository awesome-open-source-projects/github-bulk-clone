import argparse
import sys
import getpass

from . import clone_all_repos_of

def main():
    parser = argparse.ArgumentParser(description='Clone all repositories of a GitHub user.')

    parser.add_argument('username', type=str, help='The GitHub username to clone repositories from')
    parser.add_argument('clone_directory', type=str, help='The directory where the repositories will be cloned')
    parser.add_argument('-t', '--token', type=str, nargs='?', default=None,
                        help='GitHub personal access token (defaults to interactive input)')

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()

    if args.token is None:
        args.token = getpass.getpass(prompt='Enter your GitHub token: ')

    result = clone_all_repos_of(args.username, args.token, args.clone_directory)


if __name__ == "__main__":
    main()
