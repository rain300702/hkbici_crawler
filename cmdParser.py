# -*- coding: utf-8 -*-

import argparse


def depthType(rawInput):
    try:
        depth = int(rawInput)
    except ValueError:
        errMsg = 'The program only accept integer as an input.'
        errMsg += 'Please try again.'
        raise argparse.ArgumentTypeError(errMsg)
    if depth < 1:
        errMsg = 'The program only accept positive integer as an input.'
        errMsg += 'Please try again making sure that your input value is positive.'
        raise argparse.ArgumentTypeError(errMsg)
    else:
        return depth

parser = argparse.ArgumentParser(prog='hkbici-crawler', description='Crawler for hkbici by Jack', epilog='Plz don\'t abuse my username and pwd for the forum:')
parser.add_argument('-d', '--depth', default='20', type=depthType, help='Expect numeral input for searching depth')
parser.add_argument('-k', '--keyword', default='', type=str, help='Keywords for searching')
parser.add_argument('-i', '--initiation', action='store_true', help='Use this optional argument if this is your first use')

def main():
    args = parser.parse_args()
    print args

if __name__ == '__main__':
    main()
