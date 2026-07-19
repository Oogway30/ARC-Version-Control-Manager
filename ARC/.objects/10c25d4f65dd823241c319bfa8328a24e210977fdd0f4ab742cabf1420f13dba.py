import argparse
from repository import init
from objects import commit
from temporary import add,untracked_files


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
checkout_command.add_argument("-m", "--message", type=str, help="Add a message.")
checkout_command.set_defaults(func=commit)

add_command = subparsers.add_parser("add",help="Add to Temporary Storage.")
add_command.add_argument("path", type=str, help="Path to files.", nargs="*")
add_command.set_defaults(func=add)

untracked_files_command = subparsers.add_parser("untracked_Files",help="See untracked files.")
untracked_files_command.set_defaults(func=untracked_files)




args = global_parser.parse_args()
print(args.func(args))
#Something changed here!!