import argparse

parser=argparse.ArgumentParser()
parser.add_argument('-H','--host',
                    default='localhost',
                    dest='host',
                    help='Provide destination host. Default is localhost',
                    type=str)
args=parser.parse_args()
print(f'The host is "{args.host}"')

import argparse
parser=argparse.ArgumentParser()
parser.add_argument()