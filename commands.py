import argparse

parser = argparse.ArgumentParser(
                    prog='MINI - Git',
                    description='A simple version control software.',
                    epilog='if there are any other ideas, contact Oogway30 through the repository.')

parser.add_argument("req")
parser.add_argument("name")
parser.add_argument('-f', "--filename")           # positional argument
parser.add_argument('-c', '--count')      # option that takes a value
parser.add_argument('-v', '--verbose',
                    action='store_true')  # on/off flag

args = parser.parse_args()


