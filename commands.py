import argparse
from repository import init
from objects import commit,checkout
from temporary import add,untracked_files
import datetime
def build_parser():
    global_parser = argparse.ArgumentParser(
                        prog='ARC',
                        description='A simple version control software.',
                        epilog='if there are any other ideas, contact Oogway30 through the repository.')

    subparsers = global_parser.add_subparsers(
        title="BASIC COMMANDS"
    )

    initialize = subparsers.add_parser("init", help='Initialize a Repository.')
    initialize.add_argument("author", type=str, help="Add an Author of the Repository.")
    initialize.set_defaults(func=init)

    commit_command = subparsers.add_parser("commit",help="Commit to repository.")
    commit_command.add_argument("-m", "--message", type=str, help="Add a message.")
    commit_command.set_defaults(func=commit)

    checkout_command = subparsers.add_parser("checkout",help="Checkout to a commit.")
    checkout_command.add_argument("-cnr", "--commit_nr", type=int, help="Commit NR to checkout to.")
    checkout_command.set_defaults(func=checkout)

    add_command = subparsers.add_parser("add",help="Add to Temporary Storage.")
    add_command.add_argument("path", type=str, help="Path to files.", nargs="*")
    add_command.set_defaults(func=add)

    untracked_files_command = subparsers.add_parser("untracked_Files",help="See untracked files.")
    untracked_files_command.set_defaults(func=untracked_files)

    return global_parser


def main():
    parser = build_parser()
    args = parser.parse_args()
    if not hasattr(args, "func"):
        parser.print_help()
        return 1
    result = args.func(args)
    if result is not None:
        print(result)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())