# -*- coding: utf-8 -*-

from crawler import Crawler
from cmdParser import parser


def main():
    try:
        args = parser.parse_args()
        crawler = Crawler(args)
        crawler.entry()
    except KeyboardInterrupt:
        print 'Process aborted by user.'

if __name__ == '__main__':
    main()
