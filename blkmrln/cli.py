import argparse
from .commands import build

def main():
    parser = argparse.ArgumentParser(description="BLKMRLN CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Build command
    build_parser = subparsers.add_parser('build', help='Build the project')
    build_parser.add_argument('-n', '--name', required=True, help='Name of the project')

    # Rename command
    rename_parser = subparsers.add_parser('rename', help='Rename the project')
    rename_parser.add_argument('-n', '--name', required=True, help='Name of the project')
    rename_parser.add_argument('-r', '--newname', required=True, help='New name of the project')

    #Test command
    test_parser = subparsers.add_parser('test', help='Test the project')
    test_parser.add_argument('-n', '--name', required=True, help='Name of the project')

    # Parse arguments
    args = parser.parse_args()

    if args.command == 'build':
        build.execute(args)

if __name__ == "__main__":
    main()