# -*- coding: utf-8 -*-

import argparse


def numberType(rawInput):
    try:
        number = int(rawInput)
    except ValueError:
        errMsg = 'The program only accept integer as an input.'
        errMsg += 'Please try again.'
        raise argparse.ArgumentTypeError(errMsg)
    if number < 1:
        errMsg = 'The program only accept positive integer as an input.'
        errMsg += 'Please try again making sure that your input value is positive.'
        raise argparse.ArgumentTypeError(errMsg)
    else:
        return number

parser = argparse.ArgumentParser(prog='hkbici-crawler', description='Crawler for hkbici by Jack', epilog='Plz don\'t abuse my username and pwd for the forum:')
parser.add_argument('-d', '--depth', default='50', type=numberType, help='Expect numeral input for searching depth')
parser.add_argument('-k', '--keyword', default='', type=str, help='Keywords for searching')
parser.add_argument('-i', '--initiation', action='store_true', help='Use this optional argument if this is your first use')
parser.add_argument('-n','--threadNum', default='10', type = numberType, help='Expect numeral input for thread number')

def main():
    args = parser.parse_args()
    print args

if __name__ == '__main__':
    main()
